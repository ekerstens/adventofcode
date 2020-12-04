from typing import List, NamedTuple
from copy import copy
from .advent_day import AdventDay
from io import TextIOWrapper



class PasswordPolicy(NamedTuple):
    """Data object to organize password file contents."""

    min_: int
    max_: int
    letter: str
    password: str


class Day2(AdventDay):
    """Day 2 Solution"""

    _day = 2

    @staticmethod
    def format_line(line):
        """Convert a single line of text into a PasswordPolicy."""
        line = line.strip()
        return PasswordPolicy(
            min_=int(line[0 : line.find("-")]),
            max_=int(line[line.find("-") + 1 : line.find(" ")]),
            letter=line[line.find(" ") + 1 : line.find(":")],
            password=line[line.find(":") + 2 :],
        )

    def parse_input(self, input_data: TextIOWrapper) -> List[PasswordPolicy]:
        """Convert contents of input file to PasswordPolicies."""
        return [self.format_line(line) for line in input_data]

    def problem_1(self, input_list: List[PasswordPolicy]) -> int:
        def password_okay(policy: PasswordPolicy) -> bool:
            occurances = policy.password.count(policy.letter)
            return policy.min_ <= occurances <= policy.max_

        return sum([password_okay(policy) for policy in input_list])

    def problem_2(self, input_list: List[PasswordPolicy]) -> int:
        def password_okay(policy: PasswordPolicy) -> bool:
            return (policy.password[policy.min_ - 1] == policy.letter) ^ (
                policy.password[policy.max_ - 1] == policy.letter
            )

        return sum([password_okay(policy) for policy in input_list])


if __name__ == "__main__":
    Day2().results()
