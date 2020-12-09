from src.day9 import Day9

day9 = Day9(preamble=5)
test_data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_problem_1():
    assert day9.problem_1(test_data) == 127


def test_problem_2():
    assert day9.problem_2(test_data) == 62