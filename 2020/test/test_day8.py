from src.day8 import Day8, Command


day8 = Day8()
test_data = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]

formatted_data = day8.parse_input(test_data)


def test_parse_input():
    assert formatted_data == [
        Command(command="nop", value=0),
        Command(command="acc", value=1),
        Command(command="jmp", value=4),
        Command(command="acc", value=3),
        Command(command="jmp", value=-3),
        Command(command="acc", value=-99),
        Command(command="acc", value=1),
        Command(command="jmp", value=-4),
        Command(command="acc", value=6),
    ]


def test_problem_1():
    assert day8.problem_1(formatted_data) == 5


def test_problem_2():
    assert day8.problem_2(formatted_data) == 8
