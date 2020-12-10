from typing import List
from math import prod
from collections import Counter
from .advent_day import AdventDay

from pprint import pprint


class Day10(AdventDay):
    """Day10 Submission"""

    _day = 10

    def parse_input(self, input_data):
        input_values = [int(line) for line in input_data]
        return input_values + [0, max(input_values) + 3]

    @staticmethod
    def adapter_chain(adapter_ratings):
        return Counter(
            min(inc for inc in (1, 2, 3) if start + inc in adapter_ratings)
            for start in sorted(adapter_ratings)[:-1]
        )

    def count_combinations(self, start: int, adapter_ratings: List[int]):
        if start == max(adapter_ratings):
            return 1
        return sum(
            self.count_combinations(start + inc, adapter_ratings)
            for inc in (1, 2, 3)
            if start + inc in adapter_ratings
        )

    def count_combinations_non_recursive(self, adapter_ratings):
        """
        Counting all the branches recursively is very slow. From any single point n in
        the list the exact number of diret branches from point n is determined by
        whether the values n+1, n+2, n+3 are in the list. Summing the number of
        brances from each of those values in turn gives the total branching from n.

        This function iterates over the ratings in reverse to sum the total branches.
        """
        direct_brances_from_adapters = [
            sum(1 for inc in (1, 2, 3) if inc + rating in adapter_ratings)
            for rating in sorted(adapter_ratings)[:-1]
        ]
        branches = [1]
        for idx, branch in enumerate(reversed(direct_brances_from_adapters)):
            idx += 1
            total_branches = sum(branches[idx - branch : idx])
            branches.append(total_branches)
        return max(branches)

    def problem_1(self, input_data):
        joltage_differences = self.adapter_chain(input_data)
        return joltage_differences[1] * joltage_differences[3]

    def problem_2(self, input_data):
        return self.count_combinations_non_recursive(input_data)


if __name__ == "__main__":
    Day10().results()