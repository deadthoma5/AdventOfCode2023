from aocd import submit
from aocd.models import Puzzle
from functools import reduce

puzzle = Puzzle(year=2023, day=2)
puzzleInput = puzzle.input_data

# Part A
answer = 0
limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for line in puzzleInput.split('\n'):
    isPossible = True
    game = line.split(": ")
    game[0] = int(game[0].replace("Game ", ""))
    game[1] = game[1].split('; ')
    for cubeset in game[1]:
        cubes = cubeset.split(', ')
        for c in cubes:
            count, color = c.split()
            if int(count) > limits[color]:
                isPossible = False
    if isPossible:
        answer += game[0]

submit(answer, part="a", day=2, year=2023)

# Part B
answer = 0

for line in puzzleInput.split('\n'):
    minimums = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    game = line.split(": ")
    game[1] = game[1].split('; ')
    for cubeset in game[1]:
        cubes = cubeset.split(', ')
        for c in cubes:
            count, color = c.split()
            if int(count) > minimums[color]:
                minimums[color] = int(count)
    power = reduce(lambda x, y: x * y, minimums.values())
    answer += power

submit(answer, part="b", day=2, year=2023)