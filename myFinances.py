# Core objects: Goals(), Assets(), Debts(), Incomes(), Expenses()

# Inputs section - the user inserts his inputs here
# Snapshot section - the user gets a snapshot of his financial situation and a score for each segment
# Visualization section - the user can spot trends that'll help him understand where he's at and where he might be headed
# Motivation section - the user will receive quotes, book recommendations and anything that motivates him to wealth building

# Cashflow: All incomes - All expenses
# Reach positive cashflow and set aside a specific amount every month, have that invested in the all weather portfolio

import pandas as pd

myCurrency = 'ILS'
foreignCurrency = 'USD'
USDILS = 3.5


class InputError(Exception):
    """
    You have entered an incorrect input, check the type of the inputs you're trying to add.
    """


class Finances:
    pass


class Goals:
    def __init__(self):
        self.financial_security = float('NaN')
        self.financial_vitality = float('NaN')
        self.financial_independence = float('NaN')
        self.financial_freedom = float('NaN')
        self.absolute_financial_freedom = float('NaN')

    def set_goal(self, level, amount):
        # Enter level from 1 to 5
        if level == 1:
            self.financial_security = amount
        elif level == 2:
            self.financial_vitality = amount
        elif level == 3:
            self.financial_independence = amount
        elif level == 4:
            self.financial_freedom = amount
        elif level == 5:
            self.absolute_financial_freedom = amount
        else:
            raise InputError

    def show_goals(self):
        data = {
            'Financial Security': self.financial_security,
            'Financial Vitality': self.financial_vitality,
            'Financial Independence': self.financial_independence,
            'Financial Freedom': self.financial_freedom,
            'Absolute Financial Freedom': self.absolute_financial_freedom
        }
        goals = pd.Series(data)
        return goals


class Assets:
    def __init__(self):
        self.assets = []

    def add_asset(self, description, value, returns, dividend=None, currency='ILS'):
        asset = {
            'Description': description,
            'Value': value,
            'Returns': returns,
            'Dividend': dividend,
            'Currency': currency
        }
        self.assets.append(asset)

    def show_assets(self):
        pass


class Debts:
    def __init__(self):
        self.debts = []

    def add_debt(self, to, current_balance, total, current_payment, total_payments, interest=0, interval='Monthly', reason=''):
        debt = {
            'To': to,
            'Current Balance': current_balance,
            'Total': total,
            'Payment #': current_payment,
            'Total Payments': total_payments,
            'Payments Left': total_payments - current_payment,
            'Interval': interval,
            'Estimated Repayments': round((current_balance / (total_payments - current_payment)) + (interest * current_balance), 2),
            'Interest Rate': interest,
            'Reason': reason
        }
        if debt not in self.debts:
            self.debts.append(debt)

    def show_debts():
        pass


class Incomes:
    def __init__(self):
        self.incomes = []

    def add_income(self):
        pass

    # define show_incomes here


class Expenses:
    def __init__(self):
        self.expenses = []
    # Need to add timestamp as one of the inputs here

    def add_expense(self, description, category, amount, interval, isfixed=False, issubscription=False, isdebtrepayment=False):
        expense = {
            'Is Fixed': isfixed,
            'Description': description,
            'Category': category,
            'Amount': amount,
            'Interval': interval,
            'Is Subscription': issubscription,
            'Is Debt Repayment': isdebtrepayment
            # Timestamp
        }
        self.expenses.append(expense)

    def show_expenses(self):
        pass
