from src.day11 import Day11

day11 = Day11()
test_data = day11.parse_input(
    [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
)


def test_problem_1():
    assert day11.problem_1(test_data) == 37


def test_problem_2():
    assert day11.problem_2(test_data) == 26