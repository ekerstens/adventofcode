from src.day14 import Day14, Mask, Mem

day14 = Day14()
test_data = day14.parse_input(
    [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
)


def test_parse_input():
    assert test_data == [
        Mask(mask="XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
        Mem(position=8, value=11),
        Mem(position=7, value=101),
        Mem(position=8, value=0),
    ]


def test_problem_1():
    assert day14.problem_1(test_data) == 165


def test_problem_2():
    test_data = day14.parse_input(
        [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1",
        ]
    )
    assert day14.problem_2(test_data) == 208