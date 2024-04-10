# Class is an blueprint
# class name should be in pascal case - ThisIsPascalCase

#  OBJECT is the instance of the class

# making an software of ATM machine using oop

# account balance
# deposit
# withdraw
# check balance
# pin

# function vs method

# method is a special function written inside class
# len(a) #function
# a.append #method

class Atm:
    # init is contructor 
    # contructor is the special method which automatically exicute when called
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    def menu(self):
        user_input = input('''
                           Hello, how would you like to proceed
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 for withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           
                           ''')
        if user_input == "1":
            self.pin
        elif user_input =="2":
            self.balance
        elif user_input =="3":
            self.withdraw
        elif user_input == "4":
            self.check_balance
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set sucessfully")
    def deposit (self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amt = int(input("Enter the amount"))
            self.balance = self.balance + amt
            print("Deposit succesfully")
        else:
            print("Invalid pin")
    def withdraw (self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amt = int(input("Enter the amt"))
            if amt < self.balance:
                self.balance = self.balance - amt
                print("operation succesful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")
    def check_pin(self):
        print(self.pin)

        

sbi = Atm()

sbi.check_pin()