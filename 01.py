from aocd import submit
from aocd.models import Puzzle
import re

def find_first(s, pats):
    res = re.search("|".join(pats), s).group()
    return int(res) if res in pats[0] else pats.index(res)

puzzle = Puzzle(year=2023, day=1)
puzzleInput = puzzle.input_data.split('\n')

pats = ["[123456789]"]
rpats = pats
answer_a = sum(find_first(line, pats)*10 + find_first(line[::-1], rpats) for line in puzzleInput)
submit(answer_a, part="a", day=1, year=2023)

pats = "[123456789] one two three four five six seven eight nine".split()
rpats = [pats[0]] + [p[::-1] for p in pats[1:]]
answer_b = sum(find_first(line, pats)*10 + find_first(line[::-1], rpats) for line in puzzleInput)
submit(answer_b, part="b", day=1, year=2023)