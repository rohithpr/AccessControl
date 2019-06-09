"""Exceptions related to rules."""

class RuleException(Exception):
    def __init__(self, message):
        super(RuleException, self).__init__(message)


class ImplicitDenyExplictlyDeclaredException(RuleException):
    def __init__(self, action):
        message = 'An IMPLICIT_DENY was excplicitly declared. Use EXPLICIT_DENY instead.'
        super(ImplicitDenyExplictlyDeclaredException, self).__init__(message)
