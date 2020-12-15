from typing import List, Dict
from .advent_day import AdventDay


class IndexTracker:
    def __init__(self, first_index: int = None, second_index: int = None):
        self._last_index = first_index
        self.second_index = second_index

    @property
    def last_index(self):
        return self._last_index

    @last_index.setter
    def last_index(self, value):
        self.second_index = self._last_index
        self._last_index = value

    @property
    def difference(self):
        return self.last_index - self.second_index

    def singular(self) -> bool:
        """Indicates if more than one index has been set for this tracker"""
        return self.second_index is None

    def __repr__(self):
        return f"IndexTracker(last_index = {self._last_index}, second_index = {self.second_index}"


class Day15(AdventDay):
    """Day15 Submission"""

    _day = 15

    def parse_input(self, input_data) -> List[int]:
        return [int(number) for line in input_data for number in line.split(",")]

    @staticmethod
    def play_game(starting_numbers: List[int], idx_to_find: int) -> int:
        """return the result of the game at a given index"""
        numbers: Dict[int, IndexTracker] = {
            number: IndexTracker(idx) for idx, number in enumerate(starting_numbers)
        }
        current_idx = len(starting_numbers)
        last_number = starting_numbers[-1]
        last_index_tracker = numbers[last_number]
        while True:
            if current_idx == idx_to_find:
                return last_number

            last_number = (
                0 if last_index_tracker.singular() else last_index_tracker.difference
            )
            if last_number not in numbers:
                last_index_tracker = IndexTracker(current_idx)
                numbers[last_number] = last_index_tracker
            else:
                last_index_tracker = numbers[last_number]
                last_index_tracker.last_index = current_idx

            current_idx += 1

    def problem_1(self, input_data: List[int]) -> int:
        return self.play_game(input_data, 2020)

    def problem_2(self, input_data):
        return self.play_game(input_data, 30000000)


if __name__ == "__main__":
    Day15().results()