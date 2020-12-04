from src.day2 import Day2

day2 = Day2()
test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
formatted_input = day2.parse_input(test_input)


def test_problem_1():
    result = day2.problem_1(formatted_input)
    assert result == 2


def test_problem_2():
    result = day2.problem_2(formatted_input)
    assert result == 1