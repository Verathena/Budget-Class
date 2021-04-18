class Budget:
    '''This is an attempt at a budget app based on class.
Dear Zuri Mentor,
I am not entirely sure that I am doing the right thing,
please leave a generous review
so I can make necessary adjustments.
Thank you'''
    def __init__(self, amount=0, item = 'any'):
        self.amount = amount
        self.item = item

    def Withdraw(self, amount):
        self.amount -= amount

    def Deposit (self, amount):
        self.amount += amount

    def Transfer (self, amount, other):
        self.Withdraw(amount)
        self.Deposit(amount)

    def Balance (self):
        return self.amount

'''Examples '''
utility = Budget(5000, item = 'utility')
food = Budget(5000, item = 'food')
entertainment = Budget(5000, item = 'entertainment')

utility.Deposit(1000)
print('Deposit Made. Your balance is', format(utility.Balance()))        
    
food.Withdraw(3500)
print('Withdrawal Made. Your balance is', format(food.Balance()))

entertainment.Balance()
print('Your balance is', format(entertainment.Balance()))

entertainment.Transfer(2000,food)
print('Transfer Made. Your balance is', format(food.Balance()))
