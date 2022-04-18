class Account:
    def __init__(self,x,y):
        self.balance = x
        self.name=y
        self.nominee=[]
        print(self.name ," your account hass been created")

    def Deposit(self,b):
        self.balance = self.balance + b
        print(b ,"rs has been diposited")
        return self.balance


    def Withdrawal(self,c):
        self.balance = self.balance - c
        print(c, " rs has beeen widrawn from bank")
        return  self.balance

    def AddNominee(self,x):
        self.nominee.append(x)
        return self.nominee

    def __len__(self):
        print("total no of nominees are ")
        return len(self.nominee)

    def __iter__(self):
        return iter(self.nominee)

    def __str__(self):
        return f"Name = {self.name}\n available balance is  = {self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance


    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self,other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance















