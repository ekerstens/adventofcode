from abc import ABC, abstractmethod
from typing import Any
from io import TextIOWrapper


class AdventDay(ABC):
    """Base calass"""

    _day = None

    @property
    def input_file(self):
        return f"resources/day_{self.day}_input.txt"

    @property
    def day(self):
        if self._day is None:
            raise NotImplementedError("Class must define _day")
        return self._day

    def results(self):
        with open(self.input_file) as input_data:
            data = self.parse_input(input_data)
        result_1 = self.problem_1(data)
        print(f"Result 1: {result_1}")

        result_2 = self.problem_2(data)
        print(f"Result 2: {result_2}")

    @abstractmethod
    def parse_input(self, input_data: TextIOWrapper) -> Any:
        """Convert contents of input file to required form."""

    @abstractmethod
    def problem_1(self, input_data: Any) -> Any:
        """Provide the solution to problem 1."""

    @abstractmethod
    def problem_2(self, input_data: Any) -> Any:
        """Provide the solution to problem 2."""