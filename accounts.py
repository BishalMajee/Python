class Accounts:
    def __init__(self, account_no, cust_id, account_type, account_opening_date, balance):
        self.account_no = account_no
        self.cust_id = cust_id
        self.account_type = account_type
        self.account_opening_date = account_opening_date
        self.balance = balance
    
    def print_details(self):
        print(f"Account Number: {self.account_no}")
        print(f"Customer ID: {self.cust_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Opening Date: {self.account_opening_date}")
        print(f"Balance: {self.balance}")
        print("-" * 30)

def create_account():
    account_no = input("Enter Account Number: ")
    cust_id = input("Enter Customer ID: ")
    account_type = input("Enter Account Type (Savings/Checking/Fixed Deposit): ")
    account_opening_date = input("Enter Account Opening Date (YYYY-MM-DD): ")
    balance = float(input("Enter Balance: "))
    return Accounts(account_no, cust_id, account_type, account_opening_date, balance)

def main():
    num_accounts = int(input("Enter the number of accounts to create: "))
    accounts = []
    
    for _ in range(num_accounts):
        print("\nEnter details for account:")
        account = create_account()
        accounts.append(account)
    
    print("\nAccount Details:")
    for account in accounts:
        account.print_details()

if __name__ == "__main__":
    main()
