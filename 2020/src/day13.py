from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass
from .advent_day import AdventDay


@dataclass
class Day13Input:
    earliest_timestamp: int
    bus_schedules: List[Optional[int]]


@dataclass
class BusSchedule:
    frequency: int
    offset: int

    def intersect(self, schedule_2: BusSchedule) -> int:
        check_time = self.offset
        while True:
            check_time += self.frequency
            if (check_time + schedule_2.offset) % schedule_2.frequency == 0:
                return check_time


class Day13(AdventDay):
    """Day13 Submission"""

    _day = 13

    def parse_input(self, input_data) -> Day13Input:
        input_data = list(input_data)
        return Day13Input(
            int(input_data[0]),
            [
                int(schedule) if schedule.isdigit() else None
                for schedule in input_data[1].split(",")
            ],
        )

    def problem_1(self, input_data: Day13Input) -> int:
        next_bus_time = {
            bus_id: bus_id * (input_data.earliest_timestamp // bus_id + 1)
            for bus_id in input_data.bus_schedules
            if bus_id is not None
        }
        earliest_bus = min(next_bus_time, key=next_bus_time.get)
        return earliest_bus * (
            next_bus_time[earliest_bus] - input_data.earliest_timestamp
        )

    def problem_2(self, input_data: Day13Input):
        for offset, schedule in enumerate(input_data.bus_schedules):
            if offset == 0:
                schedule_1 = BusSchedule(schedule, offset)
                continue
            if schedule is None:
                continue
            schedule_2 = BusSchedule(schedule, offset)
            intersection = schedule_1.intersect(schedule_2)
            schedule_1 = BusSchedule(
                schedule_1.frequency * schedule_2.frequency, intersection
            )
        return schedule_1.offset


if __name__ == "__main__":
    Day13().results()