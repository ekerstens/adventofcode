from typing import List
from copy import copy
from io import TextIOWrapper
from math import prod
from .advent_day import AdventDay
from .utils import find_pair


class Day1(AdventDay):
    _day = 1

    def __init__(self, goal_sum: int = 2020):
        self.goal_sum = goal_sum

    def parse_input(self, input_data: TextIOWrapper) -> List[int]:
        return [int(line.strip()) for line in input_data]

    def problem_1(self, input_data: List[int]) -> int:
        pair = find_pair(self.goal_sum, input_data)
        return prod(pair)

    def problem_2(self, input_data: List[int]) -> int:
        for idx, expense in enumerate(input_data):
            remaining_sum = self.goal_sum - expense
            remaining_inputs = input_data.copy()
            remaining_inputs.pop(idx)
            pair = find_pair(remaining_sum, remaining_inputs)
            if pair is not None:
                return expense * prod(pair)


if __name__ == "__main__":
    Day1().results()