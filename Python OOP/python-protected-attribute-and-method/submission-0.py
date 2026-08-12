class Account:
    def __init__(self, title, balance):
        self.title = title
        self._balance = balance #Use underscore prefix for protected attributes during initialization
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}") #Remember you can access protected attributes within the class.


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
