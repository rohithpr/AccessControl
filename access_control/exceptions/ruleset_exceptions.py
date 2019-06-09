"""Exceptions related to rulesets."""

class RulesetException(Exception):
    def __init__(self, message):
        super(RulesetException, self).__init__(message)


class RulesetRuleTypeException(RulesetException):
    def __init__(self, obj):
        message = 'Expected rule of type Rule. Got {} of type {} instead.'.format(obj, type(obj))
        super(RulesetRuleTypeException, self).__init__(message)
