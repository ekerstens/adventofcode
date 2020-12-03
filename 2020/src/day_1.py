from typing import List
from copy import copy

goal_sum = 2020


def parse_input(input_file):
    with open(input_file) as input_data:
        return [int(line.strip()) for line in input_data]


def find_pair(goal: int, input_list: List[int]):
    for expense in input_list:
        pair_value = goal - expense
        if pair_value in input_list:
            return pair_value * expense
    return -1


def problem_1(input_list: List[int]):
    return find_pair(goal_sum, input_list)


def problem_2(input_list: List[int]):
    for idx in range(len(input_list)):
        expense = input_list[idx]
        remaining_sum = goal_sum - expense
        remaining_inputs = input_list.copy()
        remaining_inputs.pop(idx)
        sub_pair_multiple = find_pair(remaining_sum, remaining_inputs)
        if sub_pair_multiple != -1:
            return expense * sub_pair_multiple


if __name__ == "__main__":
    data = parse_input("resources/day_1_input.txt")
    result_1 = problem_1(data)
    print(f"Result 1: {result_1}")

    result_2 = problem_2(data)
    print(f"Result 2: {result_2}")