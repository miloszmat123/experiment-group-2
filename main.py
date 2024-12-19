class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print("Balance for account number" + self.account_number  + " is " + self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class AccountManager:
    
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number):
        self.accounts.append(BankAccount(account_number, 0))

    def accounts_and_balances(self):
        for account in self.accounts:
            account.display_balance()

    def transfer_money(account_n1, account_n2, amount):
        account_n1.withdraw(sum)
        account_n2.deposit(sum)


