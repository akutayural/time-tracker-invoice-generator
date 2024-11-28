from enum import Enum


class UserRole(int, Enum):
    ADMIN = 1
    TEAM_LEAD = 2
    TEAM_MEMBER = 3


class Status(str, Enum):
    ACTIVE = "ACTIVE"
    PASSIVE = "PASSIVE"
    DELETED = "DELETED"

