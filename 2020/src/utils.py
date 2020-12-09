from typing import Iterable, List, Tuple, Optional


def join_lines(lines: Iterable[str]) -> List[List[str]]:
    """Combines input data into a """
    collapsed_lines = [[]]
    terminal = False
    for line in lines:
        line = line.strip()
        if line == "":
            terminal = True
        else:
            if terminal:
                terminal = False
                collapsed_lines.append([])
            collapsed_lines[-1].append(line)
    return collapsed_lines


def find_pair(goal: int, input_list: List[int]) -> Optional[Tuple[int, int]]:
    """
    Scans a list of values for aa pair the adds to the goal.
    Returns a tuple of values that complete the sum, or None if no pair is found.
    """
    for value in input_list:
        pair_value = goal - value
        if pair_value in input_list:
            return (value, pair_value)
    return None
