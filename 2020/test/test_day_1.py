from src.day_1 import Day1

day1 = Day1()
test_input = [1721, 979, 366, 299, 675, 1456]


def test_problem_1():
    result = day1.problem_1(test_input)
    assert result == 514579


def test_problem_2():
    result = day1.problem_2(test_input)
    assert result == 241861950