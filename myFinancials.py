import pandas as pd


def Income(amount):
    income = amount
    return income


class Asset:
    def __init__(self, description, value):
        self.description = description
        self.worth = value


class Debt:
    def __init__(self, creditor, value, interest=None, paid=None, payments_left=None):
        self.creditor = creditor
        self.value = value
        self.interest = interest
        self.paid = paid
        self.payments_left = payments_left


categories = []


class Expense:
    def __init__(self, name, amount, category=None, fixed=False, recurring=False, payments_left=None):
        self.name = name
        self.amount = amount
        self.category = category
        # This will be False if the expense is not dependant on usage and True if the expense is varying.
        self.fixed = fixed
        # This is True if this is a recurring expense, default is False.
        self.recurring = recurring
        self.payments_left = payments_left
