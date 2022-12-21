from account import Account
from decimal import Decimal

account1 = Account('Zool Hilmi', Decimal('50.00'))
account1.deposit(Decimal('25'))

account2 = Account('John Green', Decimal('60.00'))
account2.deposit(Decimal('30'))

account1.balance
account2.balance
