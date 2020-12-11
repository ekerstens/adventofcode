from src.day10 import Day10

day10 = Day10()

test_data_1 = day10.parse_input([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
test_data_2 = day10.parse_input(
    [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
)
test_data_custom = day10.parse_input([1, 2, 3, 4, 5, 8])


def test_problem_1():
    assert day10.problem_1(test_data_1) == 7 * 5
    assert day10.problem_1(test_data_2) == 22 * 10


def test_problem_2():
    assert day10.problem_2(test_data_custom) == 13
    assert day10.problem_2(test_data_1) == 8
    assert day10.problem_2(test_data_2) == 19208