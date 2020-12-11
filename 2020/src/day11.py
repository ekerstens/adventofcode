from typing import List
from .advent_day import AdventDay


class Day11(AdventDay):
    """Day11 Submission"""

    _day = 11

    def __init__(self):
        self.visibility = 1
        self.filled_seat_cuttoff = 4

    def parse_input(self, input_data):
        return list(input_data)

    def scan_visible(self, search: str, row: int, col: int, layout: List[str]) -> bool:
        def scan_direction(row_direction, col_direction):
            distance = 0
            while True:
                distance += 1
                if self.visibility and distance > self.visibility:
                    return 0
                row_jitter = distance * row_direction
                col_jitter = distance * col_direction
                if not (0 <= row + row_jitter < len(layout)) or not (
                    0 <= col + col_jitter < len(layout[row + row_jitter])
                ):
                    # out of bounds
                    return 0

                in_view = layout[row + row_jitter][col + col_jitter]
                if in_view == search:
                    return 1
                if in_view != ".":
                    # Something is blocking further view
                    return 0

        count = 0
        for row_direction in (-1, 0, 1):
            for col_direction in (-1, 0, 1):
                if (row_direction, col_direction) == (0, 0):
                    continue
                count += scan_direction(row_direction, col_direction)
        return count

    def fill_seat(self, row: int, col: int, layout: List[str]) -> bool:
        seat = layout[row][col]
        if seat != "L":
            return False
        return self.scan_visible("#", row, col, layout) == 0

    def empty_seat(self, row: int, col: int, layout: List[str]) -> bool:
        seat = layout[row][col]
        if seat != "#":
            return False
        return self.scan_visible("#", row, col, layout) >= self.filled_seat_cuttoff

    def update_seats(self, layout: List[str]) -> List[str]:
        return [
            [
                "L"
                if self.empty_seat(row_idx, col_idx, layout)
                else "#"
                if self.fill_seat(row_idx, col_idx, layout)
                else seat
                for col_idx, seat in enumerate(row)
            ]
            for row_idx, row in enumerate(layout)
        ]

    @staticmethod
    def count_filled_seats(layout: List[str]) -> int:
        return sum(sum(seat == "#" for seat in row) for row in layout)

    def find_stable_seat_layout(self, layout):
        while True:
            updated_layout = self.update_seats(layout)
            if updated_layout == layout:
                break
            layout = updated_layout
        return self.count_filled_seats(layout)

    def problem_1(self, input_data):
        self.visibility = 1
        self.filled_seat_cuttoff = 4
        return self.find_stable_seat_layout(input_data)

    def problem_2(self, input_data):
        self.visibility = None
        self.filled_seat_cuttoff = 5
        return self.find_stable_seat_layout(input_data)


if __name__ == "__main__":
    Day11().results()