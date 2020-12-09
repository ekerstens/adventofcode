import re
from dataclasses import dataclass
from typing import List, Optional
from copy import deepcopy
from .advent_day import AdventDay


@dataclass
class Command:
    command: str
    value: int


class Day8(AdventDay):
    _day = 8

    def parse_input(self, input_data) -> List[Command]:
        pattern = re.compile(r"(?P<command>^[a-zA-Z]*) (?P<value>[+-][\d]*)")
        commands = []
        for command in input_data:
            match = pattern.match(command)
            commands.append(Command(match.group("command"), int(match.group("value"))))
        return commands

    def execute_commands(
        self,
        commands: List[Command],
        swap: bool = False,
        return_on_repeat: bool = True,
        idx: int = 0,
        accumulator: int = 0,
        scanned_positions=None,
    ):
        if scanned_positions is None:
            scanned_positions = set()
        while idx < len(commands):
            command = commands[idx]
            if swap and command.command in ["nop", "jmp"]:
                commands_copy = deepcopy(commands)
                commands_copy[idx].command = (
                    "noc" if command.command == "jmp" else "jmp"
                )
                swap_result = self.execute_commands(
                    commands_copy,
                    return_on_repeat=False,
                    idx=idx,
                    accumulator=accumulator,
                    scanned_positions=deepcopy(scanned_positions),
                )
                if swap_result is not None:
                    return swap_result
            if idx in scanned_positions:
                return accumulator if return_on_repeat else None
            scanned_positions.add(idx)
            if command.command == "acc":
                accumulator += command.value
            elif command.command == "jmp":
                idx += command.value - 1
            idx += 1
        return accumulator

    def problem_1(self, input_data: List[Command]) -> int:
        return self.execute_commands(input_data)

    def problem_2(self, input_data):
        return self.execute_commands(input_data, swap=True)


if __name__ == "__main__":
    Day8().results()