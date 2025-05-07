# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:

    bank_name  =''
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    
    def display(self):
        print(Bank.bank_name)

bank = Bank()
Bank.change_bank_name('Furture Bank')
bank.display()
