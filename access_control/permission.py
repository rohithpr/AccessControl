from enum import Enum

class Permission(Enum):
    ALLOW = 1
    EXPLICIT_DENY = 2
    EXPLICIT_DENY_WITH_ALERT = 3
    IMPLICIT_DENY = 4
