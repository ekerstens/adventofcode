from __future__ import annotations
from dataclasses import dataclass
import re
import math
import numpy as np
from typing import List
from .advent_day import AdventDay


@dataclass
class Instruction:
    command: str
    magnitude: int


class Position:
    compass_angles = {"E": 0, "N": 90, "W": 180, "S": 270}

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, p: Position) -> Position:
        return Position(self.x + p.x, self.y + p.y)

    def __str__(self):
        return f"Position(x={round(self.x)}, y={round(self.y)})"

    def __repr__(self):
        return str(self)

    def __eq__(self, p: Position) -> bool:
        return self.x == p.x and self.y == p.y

    def add(self, position: Position) -> None:
        self.x += position.x
        self.y += position.y

    def update(self, position: Position) -> None:
        self.x = position.x
        self.y = position.y

    @staticmethod
    def polar_to_cartesian(angle, radius) -> Position:
        """Convert polar coordinates to cartesian"""
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        return Position(x, y)

    def rotate(self, angle: float):
        """Rotate angle degrees around the unit circle"""
        new_angle = self.angle + angle
        self.update(self.polar_to_cartesian(new_angle, self.radius))

    def move(self, angle: float, radius: float):
        update = self.polar_to_cartesian(angle, radius)
        self.update(self + update)

    def compass_movement(self, direction: str, magnitude: float):
        self.move(
            self.compass_angles[direction],
            magnitude,
        )

    @property
    def radius(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    @property
    def angle(self):
        return math.degrees(np.arctan2(self.y, self.x))

    def manhattan_distance(self) -> float:
        return abs(self.x) + abs(self.y)


class Boat(Position):
    def __init__(self, starting_angle: int):
        self.angle_faced = starting_angle
        super().__init__(0, 0)

    def turn(self, instruction: Instruction) -> None:
        if instruction.command not in ("L", "R"):
            raise ValueError("Can only turn Left (L) or Right (R).")
        angular_change = instruction.magnitude * (
            1 if instruction.command == "L" else -1
        )
        self.angle_faced = self.angle_faced + angular_change % 360

    def follow_instruction(self, instruction: Instruction) -> None:
        if instruction.command in ("L", "R"):
            self.turn(instruction)
        elif instruction.command in ("E", "S", "W", "N"):
            self.compass_movement(
                instruction.command,
                instruction.magnitude,
            )
        elif instruction.command == "F":
            self.move(self.angle_faced, instruction.magnitude)
        else:
            raise ValueError("Invalid Instruction. Must be in (L, R, E, N, W, S, F).")


class WaypointBoat(Position):
    def __init__(self, waypoint: Position):
        self.waypoint = waypoint
        super().__init__(0, 0)

    def follow_instruction(self, instruction: Instruction) -> None:
        if instruction.command in ("L", "R"):
            angle = instruction.magnitude * (1 if instruction.command == "L" else -1)
            self.waypoint.rotate(angle)
        elif instruction.command in ("E", "S", "W", "N"):
            self.waypoint.compass_movement(
                instruction.command,
                instruction.magnitude,
            )
        elif instruction.command == "F":
            for _ in range(instruction.magnitude):
                self.add(self.waypoint)
        else:
            raise ValueError("Invalid Instruction. Must be in (L, R, E, N, W, S, F).")


class Day12(AdventDay):
    """Day12 Submission"""

    _day = 12

    def parse_input(self, input_data):
        def unpack_instruction(instruction: str):
            pattern = re.compile(r"(?P<command>[a-zA-Z])(?P<magnitude>\d+)")
            match = pattern.match(instruction)
            return Instruction(
                command=match.group("command"),
                magnitude=int(match.group("magnitude")),
            )

        return [unpack_instruction(line) for line in input_data]

    def problem_1(self, input_data: List[Instruction]) -> int:
        boat = Boat(starting_angle=0)
        for instruction in input_data:
            boat.follow_instruction(instruction)
        return round(boat.manhattan_distance())

    def problem_2(self, input_data):
        boat = WaypointBoat(Position(10, 1))
        for instruction in input_data:
            boat.follow_instruction(instruction)
        return round(boat.manhattan_distance())


if __name__ == "__main__":
    Day12().results()