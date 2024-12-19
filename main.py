## task 1

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



## task 2

class Task:

    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def print_task(self):
        print("Title: " + self.title)
        print("Description: " + self.description)
        print("Priority: " + self.priority) 


class ToDoList:

    def __init__(self):
        self.tasks = []
        self.tasks_completed = []

    
    def create_task(self, title, description, priority):
        self.tasks.append(Task(title, description, priority))
        print("New task added")
    
    def complete_task(self, Task):
        self.tasks.remove(Task)
        self.tasks_completed.append(Task)

    def remove_task(self, Task):
        self.tasks.remove(Task)
        print("Task deleted")

    def view_tasks(self):
        print("Tasks to do")
        for task in self.tasks:
            task.print_task()
            print("")
        print("Tasks completed")
        for task in self.tasks_completed:
            task.print_task()
            print("")