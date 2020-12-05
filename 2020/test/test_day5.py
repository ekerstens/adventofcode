from src.day5 import Day5

day5 = Day5()

test_data = {"BFFFBBFRRR": 567, "FFFBBBFRRR": 119, "BBFFBBFRLL": 820}


def test_partition_seat():
    for seat_code, seat_id in test_data.items():
        assert day5.partition_seat(seat_code) == seat_id


def test_problem_1():
    assert day5.problem_1(test_data.keys()) == max(test_data.values())