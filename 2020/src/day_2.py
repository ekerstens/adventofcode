from typing import List, NamedTuple
from copy import copy


class PasswordPolicy(NamedTuple):
    """Data object to organize password file contents."""

    min_: int
    max_: int
    letter: str
    password: str


def format_line(line):
    """Convert a single line of text into a PasswordPolicy."""
    line = line.strip()
    policy = PasswordPolicy(
        min_=int(line[0 : line.find("-")]),
        max_=int(line[line.find("-") + 1 : line.find(" ")]),
        letter=line[line.find(" ") + 1 : line.find(":")],
        password=line[line.find(":") + 2 :],
    )
    return policy


def parse_input(input_file: str) -> List[PasswordPolicy]:
    """Convert contents of input file to PasswordPolicies."""
    with open(input_file) as input_data:
        return [format_line(line) for line in input_data]


def problem_1(input_list: List[PasswordPolicy]) -> int:
    def password_okay(policy: PasswordPolicy) -> bool:
        occurances = policy.password.count(policy.letter)
        return policy.min_ <= occurances <= policy.max_

    return sum([password_okay(policy) for policy in input_list])


def problem_2(input_list: List[PasswordPolicy]) -> int:
    def password_okay(policy: PasswordPolicy) -> bool:
        return (policy.password[policy.min_ - 1] == policy.letter) ^ (
            policy.password[policy.max_ - 1] == policy.letter
        )

    return sum([password_okay(policy) for policy in input_list])


if __name__ == "__main__":
    data = parse_input("resources/day_2_input.txt")
    result_1 = problem_1(data)
    print(f"Result 1: {result_1}")

    result_2 = problem_2(data)
    print(f"Result 2: {result_2}")