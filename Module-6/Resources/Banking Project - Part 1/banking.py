class Bank:
    
    def __init__(self, holder_name, initial_deposit_balance):
        self.holder_name = holder_name
        self.balance = initial_deposit_balance #1000
        
# ostad = Bank('Rokib', 1000)

    def deposit(self, amount):
        self.balance += amount #1000
        
    
    def get_balance(self):
        return self.balance
    
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return f'insufficient balance'
        
ostad = Bank('Rokib', 1000)
print(ostad.holder_name)

        
        
# ostad = Bank('XYZ', 1000)

# print(ostad.get_balance())
# print(ostad.holder_name)
# print(ostad.balance)
