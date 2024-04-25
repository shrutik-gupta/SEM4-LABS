class BankAccount():
    def __init__(self,account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name=customer_name

    def deposit(self, amount):
        self.amount= amount
        self.balance+=self.amount
        print(self.amount,"debited succesfully")
    
    def withdraw(self, amount):
        self.amount= amount
        self.balance-=self.amount
        print(self.amount,"credited succesfully")
    
    def check_balance(self):
        print("your current balance is: ", self.balance)

c1 = BankAccount(101,12000,"02-12-2013", "Shrutik")
c1.check_balance()
c1.deposit(500)
c1.withdraw(1400)
c1.check_balance()
