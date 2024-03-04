# Create account class with 2 attributes - balance & account no
# create methods for debit, credit & printing the balance

class Account:
    def __init__ (self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amt):
        self.balance -= amt
        print (f"{amt} is debited in your account\nCurrent Balance :-{self.get_balance()}")
    
    def credit(self,amt):
        self.balance += amt
        print (f"{amt} is credited in your account\nCurrent Balance :-{self.get_balance()}")
    
    def get_balance(self):
        return self.balance

a = Account(25000,5478658)

print(a.debit(1200))
print(a.credit(16541))

print(a.get_balance())

c= Account(265447,546545465)

c.credit(54782)
c.debit(9874)

print(c.get_balance())


