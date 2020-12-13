from src.day13 import Day13, Day13Input, BusSchedule

day13 = Day13()
test_data = day13.parse_input(["939", "7,13,x,x,59,x,31,19"])


def test_parse_input():
    assert test_data == Day13Input(
        earliest_timestamp=939,
        bus_schedules=[7, 13, None, None, 59, None, 31, 19],
    )


def test_problem_1():
    assert day13.problem_1(test_data) == 295


def test_problem_2_1():
    assert day13.problem_2(test_data) == 1068781


def test_problem_2_2():
    test_data = Day13Input(None, [17, None, 13, 19])
    assert day13.problem_2(test_data) == 3417


def test_problem_2_3():
    test_data = Day13Input(None, [67, 7, 59, 61])
    assert day13.problem_2(test_data) == 754018


def test_problem_2_4():
    test_data = Day13Input(None, [67, None, 7, 59, 61])
    assert day13.problem_2(test_data) == 779210


def test_problem_2_5():
    test_data = Day13Input(None, [67, 7, None, 59, 61])
    assert day13.problem_2(test_data) == 1261476


def test_problem_2_6():
    test_data = Day13Input(None, [1789, 37, 47, 1889])
    assert day13.problem_2(test_data) == 1202161486


def test_intersect_BusSchedules():
    s1 = BusSchedule(7, 0)
    s2 = BusSchedule(13, 1)
    assert s1.intersect(s2) == 77


def test_intersect_BusSchedules_part_2():
    s1 = BusSchedule(7 * 13, 77)
    s2 = BusSchedule(59, 4)
    assert s1.intersect(s2) == 350
