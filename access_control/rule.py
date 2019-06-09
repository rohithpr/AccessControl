from .permission import Permission


class Rule:
    def __init__(self, action, permission=Permission.ALLOW, expiration=None):
        self.action = action
        self.permission = permission
        self.expiration = None
