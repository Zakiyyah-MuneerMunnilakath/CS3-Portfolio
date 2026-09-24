
class Account:
    def __init__(self, name, number, P=0.00):
        print("Ready to open an account")
        name = input("Account name: ")
        number = input ("Account number: ")
    def deposit(self, amount):
        d = P + amount
        print("Deposit successful!")
    def __str__(self):
        return self.name, self.number, self.P
        print("Account created")
    def destructor(self):
        del Account
        print("Account",self.number,"closed")

class SavingsAccount(Account):
    def __init__(self, name):
        super().__init__(name)
    def addInterest():
        
        self.__interest = interest

class Bank:
    def __init__(self, name):
        self.name = name
    def showAccounts(self):
        self.accounts = []
    def closeAccount(self, Account):
        
    def addInterest(self,):
    
    def deposit(self, number):
    
    def __del__(self):
        del Bank
        print("Thank you for banking with us!")
    
mbtc = Bank("Metrobank")
mbtc.openAccount()
mbtc.openAccount()
mbtc.showAccounts()
mbtc.deposit()
mbtc.deposit()
mbtc.addInterest()
mbtc.closeAccount()
