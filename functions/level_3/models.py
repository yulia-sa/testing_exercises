import dataclasses
import datetime
import decimal
import enum


class Currency(enum.Enum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
    AMD = "AMD"


class ExpenseCategory(enum.Enum):
    SUPERMARKET = "SUPERMARKET"
    BAR_RESTAURANT = "BAR_RESTAURANT"
    ONLINE_SUBSCRIPTIONS = "ONLINE_SUBSCRIPTIONS"
    MEDICINE_PHARMACY = "MEDICINE_PHARMACY"
    THEATRES_MOVIES_CULTURE = "THEATRES_MOVIES_CULTURE"
    TRANSPORT = "TRANSPORT"


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class BankCard:
    last_digits: str
    owner: str


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class SmsMessage:
    text: str
    author: str
    sent_at: datetime.datetime


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Expense:
    amount: decimal.Decimal
    currency: Currency
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime
    category: ExpenseCategory | None
