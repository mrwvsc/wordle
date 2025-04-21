from enum import Enum

LETTER_COUNT = 5

# Enum for letter verdicts
class LetterVerdict(Enum):
    GREEN = 1
    YELLOW = 2
    GRAY = 3

# Helper to parse verdict strings like 'gybyg'
def parse_verdict(verdict_str):
    verdict_map = {'g': LetterVerdict.GREEN, 'y': LetterVerdict.YELLOW, 'b': LetterVerdict.GRAY}
    return [verdict_map[char] for char in verdict_str.lower()]