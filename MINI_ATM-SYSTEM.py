from abc import ABC, abstractmethod

# -------------------------------
# Abstract Class
# -------------------------------
class BankAccount(ABC):
    @abstractmethod
    def Transction(self):
        pass


# -------------------------------
# Base Class
# -------------------------------
class Account:
    def __init__(self, A_name, A_number, A_amount, pin):
        self.Holder_Name = A_name
        self._Holder_Account_number = A_number
        self.__Holder_Amount = A_amount
        self.__PIN = pin
        self.Transaction_Count = 0
        self.Transaction_History = []

    def get_Amount(self):
        return self.__Holder_Amount

    def set_Amount(self, amount):
        self.__Holder_Amount = amount

    def verify_pin(self, pin):
        return self.__PIN == pin


# -------------------------------
# Child Class
# -------------------------------
class A_T_M(BankAccount, Account):

    MAX_WITHDRAW_LIMIT = 10000

    def __init__(self, A_name, A_number, A_amount, pin):
        Account.__init__(self, A_name, A_number, A_amount, pin)

    def Amount(self, amount):
        balance = self.get_Amount() + amount
        self.set_Amount(balance)
        return balance

    def Check_balance(self):
        print(f"Your account balance is: ₹{self.get_Amount()}")

    def Deposit_Amount(self, amount):
        if amount > 0:
            self.Amount(amount)
            self.Transaction_Count += 1
            self.Transaction_History.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
            self.Check_balance()
        else:
            print("Invalid deposit amount.")

    def Withdraw_Amount(self, amount):
        if amount > self.MAX_WITHDRAW_LIMIT:
            print(f"Maximum withdrawal limit is ₹{self.MAX_WITHDRAW_LIMIT}")
        elif amount > 0 and amount <= self.get_Amount():
            self.Amount(-amount)
            self.Transaction_Count += 1
            self.Transaction_History.append(f"Withdrawn ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
            self.Check_balance()
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient balance.")

    def Show_Transaction_History(self):
        if not self.Transaction_History:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for i, t in enumerate(self.Transaction_History, 1):
                print(f"{i}. {t}")
            print(f"Total Transactions: {self.Transaction_Count}")

    @classmethod
    def Bank_Name(cls):
        print("""----------
 Welcome to
 ABC Bank!
----------""")

    def Transction(self):
        # PIN Verification
        for _ in range(3):
            pin = input("Enter your ATM PIN: ")
            if self.verify_pin(pin):
                print("PIN Verified Successfully!\n")
                break
            else:
                print("Incorrect PIN.")
        else:
            print("Card Blocked! Too many wrong attempts.")
            return

        while True:
            print("\n-----------------------------")
            print("ATM MENU")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")
            print("-----------------------------")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.Check_balance()

            elif choice == "2":
                amount = float(input("Enter amount to deposit: ₹"))
                self.Deposit_Amount(amount)

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: ₹"))
                self.Withdraw_Amount(amount)

            elif choice == "4":
                self.Show_Transaction_History()

            elif choice == "5":
                print("\nThank you for using ABC Bank ATM.")
                break

            else:
                print("Invalid choice. Please try again.")


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    A_T_M.Bank_Name()

    name = input("Enter Account Holder Name: ")
    ac_number = input("Enter Account Number: ")
    balance = float(input("Enter Initial Balance: ₹"))
    pin = input("Set 4-digit ATM PIN: ")

    atm = A_T_M(name, ac_number, balance, pin)
    atm.Transction()
