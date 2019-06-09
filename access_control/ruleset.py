from .rule import Rule
from .exceptions.ruleset_exceptions import RulesetRuleTypeException
from .permission import Permission

def check_rules_are_instances_of_rule(rules):
    for rule in rules:
        if not isinstance(rule, Rule):
            raise RulesetRuleTypeException(rule)


def verify_rules_correctness(func):
    def wrapper(self, rules, *args, **kwargs):
        check_rules_are_instances_of_rule(rules)
        func(self, rules, *args, **kwargs)

    return wrapper


class Ruleset:

    @verify_rules_correctness
    def __init__(self, rules=set()):
        self.rules = set(rules)
        self.build_rules_map()

    def build_rules_map(self):
        self.rules_map = {}
        for rule in self.rules:
            self.rules_map[rule.action] = rule

    def is_action_allowed(self, action):
        evaluation_result = self.evaluate_action_permission(action)
        if evaluation_result in [Permission.ALLOW]:
            return True
        else:
            return False

    def evaluate_action_permission(self, action):
        rule = self.rules_map.get(action, None)
        if not rule:
            return Permission.IMPLICIT_DENY
        elif rule.permission == Permission.EXPLICIT_DENY_WITH_ALERT:
            print ('Create an alert and deny')
        
        return rule.permission
