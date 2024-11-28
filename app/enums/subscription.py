from enum import Enum


class SubscriptionPlan(Enum):
    BASIC = 'BASIC'
    STANDARD = 'STANDARD'
    PREMIUM = 'PREMIUM'


class SubscriptionFeeAnnually(Enum):
    BASIC = 120
    STANDARD = 550
    PREMIUM = 1050


class SubscriptionFeeMonthly(Enum):
    BASIC = 10
    STANDARD = 50
    PREMIUM = 100
