class ATM:
    def __init__(self):
        self.balance = 1000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: {self.balance} rupees")

    def deposit(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print("Incorrect PIN.")
        elif amount <= 0:
            print("Enter a valid amount.")
        else:
            self.balance += amount
            print(f"{amount} deposited successfully.")

    def withdraw(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print("Incorrect PIN.")
        elif amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def exit(self):
        print("Thank you for using the ATM.")
