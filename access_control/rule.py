from .permission import Permission
from .exceptions.rule_exceptions import ImplicitDenyExplictlyDeclaredException


class Rule:
    def __init__(self, action, permission=Permission.ALLOW, expiration=None):
        self.action = action
        self.permission = permission
        self.expiration = expiration
        self._verify_rule_correctness()

    def _verify_rule_correctness(self):
        if self.permission == Permission.IMPLICIT_DENY:
            raise ImplicitDenyExplictlyDeclaredException(self.action)
