from money import Money


class Calculator:

    def add(self, money1, money2):
        assert money1.currency == money2.currency
        return Money(money1.amount + money2.amount, money1.currency)

    def subtract(self, money1, money2):
        assert money1.currency == money2.currency
        return Money(money1.amount - money2.amount, money1.currency)

    def multiply(self, money, by):
        return Money(money.amount * by, money.currency)

    def compare(self, money1, to):
        return money1.currency == to.currency and money1.amount == to.amount