from typing import List, Set
from .advent_day import AdventDay
from .utils import join_lines

AllGroups = List[List[Set[str]]]


class Day6(AdventDay):
    "Day6 Submission"
    _day = 6

    def parse_input(self, input_data) -> AllGroups:
        collapsed_input = join_lines(input_data)
        return [[set(person) for person in group] for group in collapsed_input]

    def problem_1(self, input_data: AllGroups) -> int:
        return sum(len(set.union(*group)) for group in input_data)

    def problem_2(self, input_data: AllGroups) -> int:
        return sum(len(set.intersection(*group)) for group in input_data)


if __name__ == "__main__":
    Day6().results()