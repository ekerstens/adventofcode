import re
from .advent_day import AdventDay
from .utils import join_lines


class Day4(AdventDay):
    _day = 4

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def parse_input(self, input_data):
        pattern = r"(?P<key>[^\s]*):(?P<value>[^\s]*)"
        collapsed_input = join_lines(input_data)
        return [
            {
                match.group("key"): match.group("value")
                for line in passport
                for match in re.finditer(pattern, line)
            }
            for passport in collapsed_input
        ]

    def problem_1(self, input_data):
        def valid_passport(passport):
            return self.required_fields.issubset(set(passport.keys()))

        return sum([valid_passport(passport) for passport in input_data])

    def problem_2(self, input_data):
        def valid_passport(passport):
            def validate_height(height: str) -> bool:
                match = re.fullmatch(r"(?P<height>\d+)(?P<type>in|cm)", height)
                if match is None:
                    return False
                return (
                    match.group("type") == "cm"
                    and 150 <= int(match.group("height")) <= 193
                ) or (
                    match.group("type") == "in"
                    and 59 <= int(match.group("height")) <= 76
                )

            valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            return (
                self.required_fields.issubset(set(passport.keys()))
                and (1920 <= int(passport.get("byr")) <= 2002)
                and (2010 <= int(passport.get("iyr")) <= 2020)
                and (2020 <= int(passport.get("eyr")) <= 2030)
                and (validate_height(passport.get("hgt", "")))
                and (re.fullmatch(r"#[0-9a-f]{6}", passport.get("hcl", "")) is not None)
                and (passport.get("ecl") in valid_eye_colors)
                and (re.fullmatch(r"[0-9]{9}", passport.get("pid", "")) is not None)
            )

        return sum([valid_passport(passport) for passport in input_data])


if __name__ == "__main__":
    Day4().results()