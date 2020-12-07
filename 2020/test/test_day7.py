from src.day7 import Day7, BagRule

day7 = Day7()
test_data = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]
formatted_data = day7.parse_input(test_data)


def test_parse_input():
    assert formatted_data == {
        "bright white": BagRule(
            color="bright white",
            children={"shiny gold": 1},
            parents=["light red", "dark orange"],
        ),
        "dark olive": BagRule(
            color="dark olive",
            children={"faded blue": 3, "dotted black": 4},
            parents=["shiny gold"],
        ),
        "dark orange": BagRule(
            color="dark orange",
            children={"bright white": 3, "muted yellow": 4},
            parents=[],
        ),
        "dotted black": BagRule(
            color="dotted black", children={}, parents=["dark olive", "vibrant plum"]
        ),
        "faded blue": BagRule(
            color="faded blue",
            children={},
            parents=["muted yellow", "dark olive", "vibrant plum"],
        ),
        "light red": BagRule(
            color="light red",
            children={"bright white": 1, "muted yellow": 2},
            parents=[],
        ),
        "muted yellow": BagRule(
            color="muted yellow",
            children={"shiny gold": 2, "faded blue": 9},
            parents=["light red", "dark orange"],
        ),
        "shiny gold": BagRule(
            color="shiny gold",
            children={"dark olive": 1, "vibrant plum": 2},
            parents=["bright white", "muted yellow"],
        ),
        "vibrant plum": BagRule(
            color="vibrant plum",
            children={"faded blue": 5, "dotted black": 6},
            parents=["shiny gold"],
        ),
    }


def test_problem_1():
    assert day7.problem_1(formatted_data) == 4


def test_problem_2():
    test_data = [
        "shiny gold bags contain 2 dark red bags.",
        "dark red bags contain 2 dark orange bags.",
        "dark orange bags contain 2 dark yellow bags.",
        "dark yellow bags contain 2 dark green bags.",
        "dark green bags contain 2 dark blue bags.",
        "dark blue bags contain 2 dark violet bags.",
        "dark violet bags contain no other bags.",
    ]
    formatted_data = day7.parse_input(test_data)
    assert day7.problem_2(formatted_data) == 126