from aocd import submit
from aocd.models import Puzzle
import re
from collections import defaultdict

puzzle = Puzzle(year=2023, day=4)
puzzleInput = puzzle.input_data.split('\n')

answer = 0
counts = defaultdict(int)
for card in puzzleInput:
    id, winners, draw = re.split(': | \| ', card)
    id = int(id.replace('Card ', ''))
    counts[id] += 1
    winners = winners.split()
    draw = draw.split()
    matches = len(set(winners) & set(draw))
    for n in range(matches):
        counts[id + n + 1] += counts[id]
    answer += 2**(matches - 1) if matches >= 1 else 0
submit(answer, part="a", day=4, year=2023)

answer = sum(counts.values())
submit(answer, part="b", day=4, year=2023)