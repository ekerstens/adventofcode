from src.day3 import Day3

day3 = Day3()
test_data = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_problem_1():
    assert day3.problem_1(test_data) == 7


def test_problem_2():
    assert day3.problem_2(test_data) == 336
