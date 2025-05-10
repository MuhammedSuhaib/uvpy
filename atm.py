import inquirer
import pyfiglet
class ATM:  # First letter of class name should be capitalized
    def __init__(self):  # Constructor (same as ts/js)
        self.balance = 5000  # variables in class are called attributes or properties
        self.pin = 1234

    def check_pin(self, input_pin): # functions in class are called methods
        '''Check if the input PIN is correct.'''  #Docstring helps to debug the code using help function
        return input_pin == self.pin # this will return True / False based on the condition

    def check_balance(self): #self must be the first parameter of every method in a class
        '''Display the current balance.'''
        print(f"Your current balance is: {self.balance} rupees")

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        else:
            self.balance += amount
            print(f"{amount} deposited successfully.")
            print(f"Your current balance is: {self.balance} rupees")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"Your current balance is: {self.balance} rupees")

    def run(self):#this is out of the loop bcz it allows the user to enter the pin only once
        '''Run the ATM program.'''
        pin = int(input("Enter your PIN: "))
        if not self.check_pin(pin):# if the check_pin is not True, it will not enter the loop
            print("Incorrect PIN.")
            print("You cannot access the ATM.")
            return #return will terminate the program so that no one can access the ATM

        while True:
            print(pyfiglet.figlet_format("Welcome", font="starwars", justify="center", width=80))
            questions = [inquirer.List('choice', message="Select an option:", choices=[
                "Check Balance",
                "Deposit",
                "Withdraw",
                "Exit"
            ])]
            answers = inquirer.prompt(questions)
            choice = answers['choice']

            if choice == "Check Balance":
                self.check_balance()
            elif choice == "Deposit":
                try:
                    amount = int(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "Withdraw":
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "Exit":
                print("Thank you for using the ATM.")
                break

ATM().run()
