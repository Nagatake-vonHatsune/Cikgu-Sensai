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


# INTERIM (Stage 2 clean-up, Part 1 only): the 31 new core rows L-1273 to L-1303 are in the ledger copy but not yet in any unit
# (Part 5 puts them in). Part 5 deletes this set and the lines that use it.
PENDING_NEW_CORE = frozenset(['L-1273', 'L-1274', 'L-1275', 'L-1276', 'L-1277', 'L-1278', 'L-1279', 'L-1280', 'L-1281', 'L-1282', 'L-1283', 'L-1284', 'L-1285', 'L-1286', 'L-1287', 'L-1288', 'L-1289', 'L-1290', 'L-1291', 'L-1292', 'L-1293', 'L-1294', 'L-1295', 'L-1296', 'L-1297', 'L-1298', 'L-1299', 'L-1300', 'L-1301', 'L-1302', 'L-1303'])
