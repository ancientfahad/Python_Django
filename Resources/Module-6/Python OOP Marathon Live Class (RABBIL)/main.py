class DBBL:

    __balance = 0

    def deposit(self,taka):
        if taka<=0:
            print("Invalid deposit amount")
        else:
            self.__balance +=taka
            print("Deposit Success")

    def withdraw(self,taka):
        if taka<=0:
            print("Inavlid withdraw")
        elif taka>self.__balance:
            print("Insufficient Fund")
        else:
            self.__balance -=taka
            print("Withdraw Success")

    def check(self):
        print(f"My Balance is {self.__balance}")


OBJ = DBBL()

OBJ.check()
OBJ.deposit(100)
OBJ.check()
OBJ.withdraw(200)
OBJ.check()