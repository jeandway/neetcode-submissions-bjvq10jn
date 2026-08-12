class BankAccount:
    def __init__(self, balance: int):
     # Add private balance
     self.__balance = balance
    
    # TODO: Add getter method for balance
    def get_balance(self) -> int:
        return self.__balance

    # TODO: Add setter method for balance
    def set_balance(self, new_balance: int) -> none:
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Cannot set negative balance!")
"""
a common good practice is to check the invalid case first and exit early.
def set_balance(self, new_balance: int) -> None:
    if new_balance < 0:
        print("Cannot set negative balance!")
        return

    self.__balance = new_balance
"""
#Outside code
#    ↓
#get_balance()       ← public door ✅ -> can print using getter instead of printing directly
#    ↓
#self.__balance      ← private data
# Don't modify the code below this line

account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
