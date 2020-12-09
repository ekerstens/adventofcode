from typing import List, Optional
from collections import deque
from .advent_day import AdventDay
from .utils import find_pair


class Day9(AdventDay):
    """Day9 Solution"""

    _day = 9

    def __init__(self, preamble: int = 25):
        self.preamble = preamble

    def parse_input(self, input_data):
        return [int(line) for line in input_data]

    def find_rule_breaker(self, input_data):
        previous_items = deque(input_data[: self.preamble], maxlen=self.preamble)
        for item in input_data[self.preamble :]:
            pair = find_pair(item, previous_items)
            if pair is None:
                return item
            previous_items.append(item)

    @staticmethod
    def find_contiguous_sum(goal: int, input_data: List[int]) -> Optional[List[int]]:
        """Must span atleast two numbers"""
        for idx, value in enumerate(input_data):
            aggregate = value
            values = [value]
            for additional_value in input_data[idx + 1 :]:
                aggregate += additional_value
                if aggregate > goal:
                    break
                values.append(additional_value)
                if aggregate == goal:
                    return values
        return None

    def problem_1(self, input_data):
        return self.find_rule_breaker(input_data)

    def problem_2(self, input_data):
        rule_breaker = self.find_rule_breaker(input_data)
        contiguous_elements = self.find_contiguous_sum(rule_breaker, input_data)
        return min(contiguous_elements) + max(contiguous_elements)


if __name__ == "__main__":
    Day9().results()