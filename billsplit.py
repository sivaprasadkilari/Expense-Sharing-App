from collections import defaultdict

class BillSplitter:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, name):
        self.users[name] = 0

    def add_expense(self, payer, amount, participants):
        if payer not in self.users:
            print(f"Error: Payer '{payer}' does not exist.")
            return
        total_participants = len(participants)
        if total_participants == 0:
            print("Error: At least one participant is required.")
            return
        individual_share = amount / total_participants
        self.users[payer] += amount
        for participant in participants:
            if participant not in self.users:
                print(f"Error: Participant '{participant}' does not exist.")
                return
            self.users[participant] -= individual_share
        self.expenses.append({
            'payer': payer,
            'amount': amount,
            'participants': participants
        })

    def print_balances(self):
        print("Current Balances:")
        for user, balance in self.users.items():
            print(f"{user}: {balance}")

    def settle_expenses(self):
        debts = defaultdict(float)
        for user, balance in self.users.items():
            if balance > 0:
                debts[user] = balance
            elif balance < 0:
                for creditor, amount in debts.items():
                    if amount >= abs(balance):
                        print(f"{user} owes {creditor}: {abs(balance)}")
                        debts[creditor] -= abs(balance)
                        break
                    else:
                        print(f"{user} owes {creditor}: {amount}")
                        balance += amount
                        debts[creditor] = 0
            if balance == 0:
                break

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add User")
            print("2. Add Expense")
            print("3. Print Balances")
            print("4. Settle Expenses")
            print("5. Exit")
            choice = input("Enter your choice (1-5):")
            if choice == '1':
                name = input("Enter user name: ")
                self.add_user(name)
            elif choice == '2':
                payer = input("Enter payer's name: ")
                amount_input = input("Enter the expense amount: ")
                try:
                    amount = float(amount_input)
                except ValueError:
                    print("Error: Please enter a valid number for the expense amount.")
                    continue
                participants_str = input("Enter participants names (comma-separated): ")
                participants = [p.strip() for p in participants_str.split(',')]
                self.add_expense(payer, amount, participants)
            elif choice == '3':
                self.print_balances()
            elif choice == '4':
                self.settle_expenses()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    bill_splitter = BillSplitter()
    bill_splitter.run()