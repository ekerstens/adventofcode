from src.day6 import Day6

day6 = Day6()
test_data = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
    "",
]
formatted_data = day6.parse_input(test_data)


def test_problem_1():
    assert day6.problem_1(formatted_data) == 11


def test_problem_2():
    assert day6.problem_2(formatted_data) == 6