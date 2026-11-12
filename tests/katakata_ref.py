"""Facts read straight from the pinned Kata-Kata chapter files (curriculum/reference/katakata/c01.json to c09.json, Kata-Kata
34710c6), so a test compares the built text with the file and not with a number typed in once and left to go stale. Independent
of the suite helpers that produce the text."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def pack(n):
    return json.loads((ROOT / f'curriculum/reference/katakata/c{n:02}.json').read_text(encoding='utf-8'))


def sedia_count(n):
    return len(pack(n)['sedia_kelas']['cards'])


def card_count(n):
    return len(pack(n)['cards'])


def last_own_card(n):
    return max(int(c['id'][-3:]) for c in pack(n)['cards'] if c['id'].startswith(f'ms-c{n:02}-'))
