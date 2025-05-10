import inquirer
import pyfiglet
from colorama import Fore, Style, init


class ATM:  # First letter of class name should be capitalized
    def __init__(self):  # Constructor (same as ts/js)
        self.balance = 5000  # variables in class are called attributes or properties
        self.pin = 1234

    def check_pin(self, input_pin):  # functions in class are called methods
        '''Check if the input PIN is correct.'''  # Docstring helps to debug the code using help function
        return input_pin == self.pin  # this will return True / False based on the condition

    def check_balance(self):  # self must be the first parameter of every method in a class
        '''Display the current balance.'''
        print(
            f"Your current balance is: {Fore.YELLOW} {self.balance} rupees 💰")

    def deposit(self, amount):
        if amount <= 0:
            print(Fore.LIGHTRED_EX + "Enter a valid amount.")
            print(Style.RESET_ALL)
        else:
            self.balance += amount
            print(f"{Fore.GREEN}{amount} deposited successfully.💲💲💲")
            print(Style.RESET_ALL)
            print(f"Your current balance is: {Fore.YELLOW} {self.balance} rupees 💵")

    def withdraw(self, amount):
        if amount <= 0:
            print(Fore.LIGHTRED_EX + "Enter a valid amount.")
            print(Style.RESET_ALL)
        elif amount > self.balance:
            print(Fore.LIGHTRED_EX + "Insufficient balance.")
            print(Style.RESET_ALL)
        else:
            self.balance -= amount
            print(f"{Fore.LIGHTMAGENTA_EX}{amount} withdrawn successfully.💸💸💸")
            print(Style.RESET_ALL)
            print(f"Your current balance is: {Fore.YELLOW} {self.balance} rupees 💵")

    def run(self):  # this is out of the loop bcz it allows the user to enter the pin only once
        '''Run the ATM program.'''
        pin = int(input(Fore.GREEN+"Enter your PIN: "))
        # if the check_pin is not True, it will not enter the loop
        if not self.check_pin(pin):
            print(Fore.LIGHTRED_EX + "Incorrect PIN.")
            print(Fore.LIGHTRED_EX + "You cannot access the ATM.")
            print(Style.RESET_ALL)
            return  # return will terminate the program so that no one can access the ATM
        welcome_text = pyfiglet.figlet_format("Welcome", font="starwars", justify="center", width=80)
        print(Fore.CYAN + welcome_text + Style.RESET_ALL)  
        while True:
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
                    print(Fore.LIGHTRED_EX + "Please enter a valid number.")
                    print(Style.RESET_ALL)
            elif choice == "Withdraw":
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print(Fore.LIGHTRED_EX + "Please enter a valid number.")
                    print(Style.RESET_ALL)
            elif choice == "Exit":
                print(Fore.GREEN + "Thank you for using the ATM.")
                print(Style.RESET_ALL)
                break

ATM().run()
