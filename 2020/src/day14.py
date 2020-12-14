import re
from dataclasses import dataclass
from typing import Union, List
import itertools
from .advent_day import AdventDay


@dataclass
class Mask:
    mask: int

    @staticmethod
    def from_re(regex: str):
        pattern = re.compile(r"^mask = (?P<mask>.*)$")
        match = pattern.match(regex)
        if match is None:
            raise ValueError("Not a mask")
        return Mask(match.group("mask"))

    @property
    def and_mask(self):
        return int(self.mask.replace("X", "1"), 2)

    @property
    def or_mask(self):
        return int(self.mask.replace("X", "0"), 2)

    def mask_value(self, value: int) -> int:
        return (value & self.and_mask) | self.or_mask

    def mask_position(self, position: int) -> List[int]:
        def single_point_mask(swap_idx, zero_at_idx: bool):
            return int(
                "".join(
                    [
                        str(1 ^ zero_at_idx)
                        if bit_idx == swap_idx
                        else str(0 ^ zero_at_idx)
                        for bit_idx in range(len(self.mask))
                    ]
                ),
                2,
            )

        mask_ones = position | int(self.mask.replace("X", "0"), 2)
        output_positions = [mask_ones]
        for idx, mask_point in enumerate(self.mask):
            if mask_point != "X":
                continue
            x_mask_zero = single_point_mask(idx, True)
            x_mask_one = single_point_mask(idx, False)
            new_positions = []
            for output in output_positions:

                new_positions.append(output | x_mask_one)
                new_positions.append(output & x_mask_zero)

            output_positions = new_positions

        return output_positions


@dataclass
class Mem:
    position: int
    value: int

    @staticmethod
    def from_re(regex: str):
        pattern = re.compile(r"^mem\[(?P<position>\d+)\] = (?P<value>\d+)$")
        match = pattern.match(regex)
        if match is None:
            raise ValueError("Not a mem command")
        return Mem(
            position=int(match.group("position")), value=int(match.group("value"))
        )


class Day14(AdventDay):
    """Day14 Submission"""

    _day = 14

    def parse_input(self, input_data) -> List[Union[Mask, Mem]]:
        return [
            Mask.from_re(line) if "mask" in line else Mem.from_re(line)
            for line in input_data
        ]

    def problem_1(self, input_data):
        address_space = {}
        for command in input_data:
            if isinstance(command, Mask):
                mask = command
            elif isinstance(command, Mem):
                address_space[command.position] = mask.mask_value(command.value)

        return sum(address_space.values())

    def problem_2(self, input_data):
        address_space = {}
        for command in input_data:
            if isinstance(command, Mask):
                mask = command
            elif isinstance(command, Mem):
                positions = mask.mask_position(command.position)
                for position in positions:
                    address_space[position] = command.value

        return sum(address_space.values())


if __name__ == "__main__":
    Day14().results()