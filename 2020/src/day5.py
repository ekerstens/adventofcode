from __future__ import annotations
from .advent_day import AdventDay
from dataclasses import dataclass
from typing import List
from pprint import pprint


@dataclass
class Seat:
    row: int
    column: int

    @property
    def seat_id(self) -> int:
        return self.row * 8 + self.column

    @classmethod
    def from_seat_code(
        cls, seat_code: str, plane_rows: int, plane_columns: int
    ) -> Seat:
        # Get row
        rows = SeatRange(0, plane_rows - 1)
        for letter in seat_code[:7]:
            rows = rows.lower_range if letter == "F" else rows.upper_range

        # Get column
        columns = SeatRange(0, plane_columns - 1)
        for letter in seat_code[7:]:
            columns = columns.upper_range if letter == "R" else columns.lower_range

        return cls(row=rows.value, column=columns.value)


class SeatFactory:
    def __init__(self, rows, columns):
        self.plane_rows = rows
        self.plane_columns = columns

    def from_code(self, seat_code: str) -> Seat:
        return Seat.from_seat_code(seat_code, self.plane_rows, self.plane_columns)


@dataclass
class SeatRange:
    """Class for tracking a range of seats used for partitioning"""

    lower_bound: int
    upper_bound: int

    @property
    def lower_midpoint(self) -> int:
        return (self.lower_bound + self.upper_bound) // 2

    @property
    def lower_range(self) -> SeatRange:
        """Return the lower half of the seat range."""
        return SeatRange(lower_bound=self.lower_bound, upper_bound=self.lower_midpoint)

    @property
    def upper_range(self) -> SeatRange:
        """Return the upper half of the seat range."""
        return SeatRange(
            lower_bound=self.lower_midpoint + 1, upper_bound=self.upper_bound
        )

    @property
    def value(self) -> int:
        if self.lower_bound == self.upper_bound:
            return self.lower_bound
        raise ValueError("SeatRange covers multiple values.")


class Day5(AdventDay):
    """Solution for day 5"""

    _day = 5

    def __init__(self, rows=128, columns=8):
        self.plane_rows = rows
        self.plane_columns = columns
        self.seat_factory = SeatFactory(rows, columns)

    def parse_input(self, input_data):
        return [line.strip() for line in input_data]

    def problem_1(self, input_data: List[str]) -> int:
        """Find the largest seat code"""
        return max(
            self.seat_factory.from_code(seat_code).seat_id
            for seat_code in input_data
        )

    def problem_2(self, input_data) -> int:
        """Return my plane seat"""
        plane_seats = [
            [None for _ in range(self.plane_columns)] for _ in range(self.plane_rows)
        ]
        for seat_code in input_data:
            seat = self.seat_factory.from_code(seat_code)
            plane_seats[seat.row][seat.column] = seat.seat_id
        all_ids = [seat_id for row in plane_seats for seat_id in row]

        for row_idx, row in enumerate(plane_seats):
            for col_idx, seat in enumerate(row):
                if seat is None:
                    # Seat isn't taken
                    potential_seat = Seat(row_idx, col_idx)
                    if (
                        potential_seat.seat_id - 1 in all_ids
                        and potential_seat.seat_id + 1 in all_ids
                    ):
                        # Seat is my seat
                        return potential_seat.seat_id
        return -1


if __name__ == "__main__":
    Day5().results()
