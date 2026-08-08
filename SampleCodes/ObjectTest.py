class Account:
    balance=0  #State (data members)
    print("b1 =",balance)
#Constructor
    def __init__(self, balance):
        print("b8 =", balance)
        Account.balance = balance
        print("b2 =",Account.balance)

    #Behavior
    def deposit(self, amount):
        self.amount=amount
        acc1.total1 = acc1.total1 + self.amount
        print("b3 =", acc1.total1)
        print("5", self.amount)
        print("ds =", (self.deposit))
        print("b4 =", self.balance)
        acc1.total1 = acc1.total1 + Account.balance

        return Account.balance + self.amount


    def checkBalance(self):
        return self.balance





#Creating objects
acc1 = Account(1000)
acc1.total1=Account.balance
print("b6 =", acc1.total1)
acc2 = Account(2000)


acc1.deposit(500)
print("b5 =", acc1.total1)
#acc1.total1=acc1.total1+Account.balance
print("acc1 balance =", acc1.total1)
print(acc2.checkBalance())


