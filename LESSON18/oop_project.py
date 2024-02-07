from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Robbin = BankAccount(2000, "Robin")

Dave.getBalance()
Robbin.getBalance()

Robbin.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(1000, Robbin)
Dave.transfer(100, Robbin)

jimmy = InterestRewardsAcct(1000, "jimmy")

jimmy.getBalance()

jimmy.deposit(100)

jimmy.transfer(100, Dave)

Roy = SavingsAcct(1000, "Roy")

Roy.getBalance()

Roy.deposit(100)

Roy.transfer(10000, Robbin)
Roy.transfer(1000, Robbin)
