from src.day_2 import problem_1, problem_2, format_line

test_input = [1721, 979, 366, 299, 675, 1456]

test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
formatted_input = [format_line(line) for line in test_input]


def test_problem_1():
    result = problem_1(formatted_input)
    assert result == 2


def test_problem_2():
    result = problem_2(formatted_input)
    assert result == 1