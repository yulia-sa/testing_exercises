import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test__parse_ineco_expense():
    cards = [BankCard("7711", "Jake Santos"),
             BankCard("6633", "Annie Kennedy"),
             BankCard("4422", "Jack Pearson")]

    sms = SmsMessage("12.99 €, card_4422 19.11.23 18:22 Brook's Grocery authcode 9090 XXX",
                     "The Ocean Bank",
                     datetime.datetime(2023, 11, 19, 18, 25))

    expense = parse_ineco_expense(sms, cards)

    assert expense == Expense(amount=decimal.Decimal('12.99'),
                              card=BankCard(last_digits='4422', owner='Jack Pearson'),
                              spent_in="Brook's Grocery",
                              spent_at=datetime.datetime(2023, 11, 19, 18, 22))

    assert expense.amount == decimal.Decimal('12.99')
    assert expense.card.last_digits == '4422'
    assert expense.card.owner == 'Jack Pearson'
    assert expense.spent_in == "Brook's Grocery"
    assert expense.spent_at == datetime.datetime(2023, 11, 19, 18, 22)
