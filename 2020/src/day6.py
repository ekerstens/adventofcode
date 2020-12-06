from .advent_day import AdventDay
from typing import List, Set

AllGroups = List[List[Set[str]]]


class Day6(AdventDay):
    _day = 6

    def parse_input(self, input_data) -> AllGroups:
        all_groups = []
        group = []
        for line in input_data:
            line = line.strip()
            if line == "":
                all_groups.append(group)
                group = []
            else:
                group.append(set(line))

        if group != []:
            all_groups.append(group)
        return all_groups

    def problem_1(self, input_data: AllGroups) -> int:
        return sum([len(set.union(*group)) for group in input_data])

    def problem_2(self, input_data: AllGroups) -> int:
        return sum([len(set.intersection(*group)) for group in input_data])


if __name__ == "__main__":
    Day6().results()