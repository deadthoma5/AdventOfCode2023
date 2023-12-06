from aocd import submit
from aocd.models import Puzzle
import math
import re

puzzle = Puzzle(year=2023, day=6)
puzzleInput = puzzle.input_data.split('\n')

def countWins(time, record):
    wins = 0
    for t in range(time + 1):
        distance = (time - t) * t
        wins += 1 if distance > record else 0
    return wins

times = list(map(int, re.findall(r'\d+', puzzleInput[0])))
records = list(map(int, re.findall(r'\d+', puzzleInput[1])))
answer = math.prod(countWins(time, record) for time, record in zip(times, records))
submit(answer, part="a", day=6, year=2023)

time = int(''.join(re.findall(r'\d+', puzzleInput[0])))
record = int(''.join(re.findall(r'\d+', puzzleInput[1])))
answer = countWins(time, record)
submit(answer, part="b", day=6, year=2023)