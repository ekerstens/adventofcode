from typing import Iterable, List


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
