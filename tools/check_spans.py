"""Check every «…» span in a file (or stdin) at one chapter before it goes into a suite.

Usage: python3 tools/check_spans.py CHAPTER FILE      (FILE may be - for stdin)

Prints each span that has a violation (affix gate, placement, Malaysian form) or a ledger gap, using the same Checker as
the build. Register pairs are not reported here (they depend on the order of the components); the build checks them.
Used for Stage 2 chapter 10 (build step 4); chapters 11 to 17 run it on each unit file before building.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from language_checks import Checker  # noqa: E402


def main():
    ch = int(sys.argv[1])
    src = sys.stdin.read() if sys.argv[2] == '-' else Path(sys.argv[2]).read_text(encoding='utf-8')
    checker = Checker(ROOT)
    spans = list(dict.fromkeys(re.findall(r'«([^«»‹›]+)»', src)))
    bad = 0
    for sp in spans:
        r = checker.inspect([{'unit': 'check', 'chapter': ch, 'source': 'span', 'source_text': 'spoken ' + sp,
                              'kind': 'model', 'text': sp}])
        v = [(e['term'], e['reasons'][0]) for e in r['violations'].values() if e['check'] != 'register']
        g = [e['term'] for e in r['ledger_gaps'].values()]
        if v or g:
            bad += 1
            print('✗', sp, '|', v, '| gaps:', g)
    print(f'{len(spans)} spans, {bad} with problems')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
