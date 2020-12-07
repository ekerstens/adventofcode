from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import List, Dict
from .advent_day import AdventDay


@dataclass()
class BagRule:
    """Node in bag tree"""

    color: str
    children: Dict[BagRule, int] = field(default_factory=list)
    parents: List = field(default_factory=list)


class Day7(AdventDay):
    """Day 7 Solution"""

    _day = 7

    def parse_input(self, input_data):
        bag_rules = {}
        base_rule_pattern = r"^(?P<rule_color>[a-zA-Z\s]*)(?= bags contain)"
        child_rule_pattern = r"(?P<count>\d+) (?P<rule_color>[a-zA-Z\s]*)(?= bag)"
        for line in input_data:
            line = line.strip()
            rule_color = re.search(base_rule_pattern, line).group("rule_color")
            children_rules = re.finditer(child_rule_pattern, line)
            rule = BagRule(
                color=rule_color,
                children={
                    match.group("rule_color"): int(match.group("count"))
                    for match in children_rules
                },
                parents=[]
                if rule_color not in bag_rules
                else bag_rules[rule_color].parents,
            )
            for child in rule.children:
                if child in bag_rules:
                    bag_rules[child].parents.append(rule.color)
                else:
                    bag_rules[child] = BagRule(color=child, parents=[rule.color])
            bag_rules[rule.color] = rule
        return bag_rules

    def problem_1(self, input_data):
        def count_parents(rule_name, all_rules):
            """Collect a unique set of parent nodes including self"""
            rule = all_rules[rule_name]
            if rule.parents == []:
                return {rule.color}
            result = {
                parent_set
                for parent in rule.parents
                for parent_set in count_parents(parent, all_rules)
            }
            result.add(rule.color)
            return result

        return len(count_parents("shiny gold", input_data)) - 1

    def problem_2(self, input_data):
        def count_children(rule_name, all_rules):
            """Count all child bags and self"""
            rule = all_rules[rule_name]
            if rule.children == {}:
                return 1
            return (
                sum(
                    count_children(child, all_rules) * count
                    for child, count in rule.children.items()
                )
                + 1
            )

        return count_children("shiny gold", input_data) - 1


if __name__ == "__main__":
    Day7().results()