from src.day15 import Day15

day15 = Day15()


def test_parse_input():
    test_data = day15.parse_input(["0,3,6"])
    assert test_data == [0, 3, 6]


def test_problem_1():
    test_data = day15.parse_input(["0,3,6"])
    assert day15.problem_1(test_data) == 436
