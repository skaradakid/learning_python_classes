#Define the BankAccount class with a private attribute __balance
class BankAccount:
    """to learn Encapsulation i to on the test of creating a Banking program
    """
    #Add a constructor to initialize the account with a starting balance.
    def __init__(self, name, balance=0, transactions={}, count=0):
        self.name = name
        self.__balance = balance
        self.transactions = transactions
        self.count = count

    #Implement deposit() method to increase the balance.
    def deposit(self,amount):
        self.amount = amount
        self.__balance += amount
        self.count += 1
        self.transactions[f"transaction{self.count}"] = ["deposited",amount]

    #Implement withdraw() method to decrease the balance.
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("balance is insuficient")
        else:
            self.__balance -= amount
            self.count +=1
            self.transactions[f"transaction{self.count}"] = ["withdrew",amount]


    #Use getter and setter methods to access and modify the balance safely.
    def getter(self):
        print(f"{self.name}, your balance is R{self.__balance}")

    def setter(self,balance):
        if balance < 0:
            print("error... balance can not be in the negative")
        else:
            self.__balance = balance
    
    #A method to transfer money between two accounts.
    def transfer(self, reciever, amount):
        if self.__balance < amount:
            print("isufficient funds for transfare")
        else:
            reciever.__balance += amount
            self.__balance -= amount
            self.count +=1
            self.transactions[f"transaction{self.count}"] = ["transfered",amount, f"To: {reciever.name}"]

    #Track the number of transactions made.
    def check_transactions(self):
        print(f"\n{self.name}, below is your transections:")
        for x, y in self.transactions.items():
            print(x, y)
        print("\r")