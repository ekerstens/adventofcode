from src.day_1 import problem_1, problem_2

test_input = [1721, 979, 366, 299, 675, 1456]


def test_problem_1():
    result = problem_1(test_input)
    assert result == 514579


def test_problem_2():
    result = problem_2(test_input)
    assert result == 241861950