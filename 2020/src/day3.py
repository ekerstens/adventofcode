from typing import List
from .advent_day import AdventDay
import numpy


class Day3(AdventDay):
    """Day 3 Solution"""

    _day = 3

    def parse_input(self, input_data):
        """Convert contents of input file to Grid."""
        return [line.strip() for line in input_data]

    @staticmethod
    def traverse_trees(row_speed: int, column_speed: int, forest: List[str]):
        width = len(forest[0])
        column = collisions = 0
        rows_encounted = [row for idx, row in enumerate(forest) if idx % row_speed == 0]
        for trees in rows_encounted:
            if trees[column] == "#":
                collisions += 1
            column += column_speed
            if column >= width:
                column = column % width
        return collisions

    def problem_1(self, input_data: List[str]) -> int:
        return self.traverse_trees(1, 3, input_data)

    def problem_2(self, input_data: List[str]) -> int:
        speeds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        collisions = [
            self.traverse_trees(row_speed, column_speed, input_data)
            for column_speed, row_speed in speeds
        ]
        return numpy.prod(collisions)


if __name__ == "__main__":
    Day3().results()
