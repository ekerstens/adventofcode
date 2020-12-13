from src.day12 import Day12, Instruction

day12 = Day12()
test_data = day12.parse_input(
    [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]
)


def test_parse_input():
    assert test_data == [
        Instruction(command="F", magnitude=10),
        Instruction(command="N", magnitude=3),
        Instruction(command="F", magnitude=7),
        Instruction(command="R", magnitude=90),
        Instruction(command="F", magnitude=11),
    ]


def test_problem_1():
    assert day12.problem_1(test_data) == 25


def test_problem_2():
    assert day12.problem_2(test_data) == 286


def test_problem_2_complex():
    complex_test_data = day12.parse_input(
        [
            "W5",
            "F63",
            "S1",
            "L90",
            "F89",
            "W4",
            "F45",
            "W4",
            "F71",
            "R90",
            "S4",
            "F16",
        ]
    )
    assert day12.problem_2(complex_test_data) == 1505
