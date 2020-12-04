from typing import List
from copy import copy
from advent_day import AdventDay
from io import TextIOWrapper

goal_sum = 2020


class Day1(AdventDay):
    _day = 1

    def parse_input(self, input_data: TextIOWrapper) -> List[int]:
        return [int(line.strip()) for line in input_data]

    def find_pair(self, goal: int, input_list: List[int]):
        for expense in input_list:
            pair_value = goal - expense
            if pair_value in input_list:
                return pair_value * expense
        return -1

    def problem_1(self, input_data: List[int]) -> int:
        return self.find_pair(goal_sum, input_data)

    def problem_2(self, input_data: List[int]) -> int:
        for idx, expense in enumerate(input_data):
            remaining_sum = goal_sum - expense
            remaining_inputs = input_data.copy()
            remaining_inputs.pop(idx)
            sub_pair_multiple = self.find_pair(remaining_sum, remaining_inputs)
            if sub_pair_multiple != -1:
                return expense * sub_pair_multiple


if __name__ == "__main__":
    Day1().results()
    # data = parse_input("resources/day_1_input.txt")
    # result_1 = problem_1(data)
    # print(f"Result 1: {result_1}")

    # result_2 = problem_2(data)
    # print(f"Result 2: {result_2}")