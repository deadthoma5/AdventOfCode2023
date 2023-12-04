from aocd import submit
from aocd.models import Puzzle
import math
import re

puzzle = Puzzle(year=2023, day=3)
grid = puzzle.input_data.split('\n')

symbols = {(r, c): [] for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] not in "0123456789."}

for r, row in enumerate(grid):
    for num in re.finditer(r'\d+', row):
        edge = {(r, c) for r in range(r-1, r+2) for c in range(num.start()-1, num.end()+1)}
        for match in edge & symbols.keys():
            symbols[match].append(int(num.group()))

answer = sum(sum(p) for p in symbols.values())
submit(answer, part="a", day=3, year=2023)

answer = sum(math.prod(v) for k, v in symbols.items() if grid[k[0]][k[1]] == '*' and len(v)==2)
submit(answer, part="b", day=3, year=2023)