# --- GLOBAL MOCK DATABASE ---
account_database = {
    "holder": "Amit Sharma",
    "balance": 25000
}

def show_balance():
    print(f"\nAccount Holder: {account_database['holder']}")
    print(f"Current Balance: ₹{account_database['balance']}")

def deposit(amount):
    if amount > 0:
        account_database["balance"] += amount
        print(f"\nSuccess! Deposited ₹{amount:.2f}.")
        print(f"New Balance: ₹{account_database['balance']:.2f}")
    else:
        print("\nError: Deposit amount must be greater than zero.")

def withdraw(amount):
    if amount > 0:
        if amount <= account_database["balance"]:
            account_database["balance"] -= amount
            print(f"\nSuccess! Withdrew ₹{amount:.2f}.")
            print(f"New Balance: ₹{account_database['balance']:.2f}")
        else:
            print("\nError: Insufficient funds!")
    else:
        print("\nError: Withdrawal amount must be greater than zero.")


while True:
    print("\n=== WELCOME TO NEOBANK CORE ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Shutdown Server")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        show_balance()
        
    elif choice == '2':
        try:
            amt = float(input("Enter amount to deposit: ₹"))
            deposit(amt)
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")
            
    elif choice == '3':
        try:
            amt = float(input("Enter amount to withdraw: ₹"))
            withdraw(amt)
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")
            
    elif choice == '4':
        print("\nShutting down server. Goodbye!")
        break 
        
    else:
        print("\nInvalid selection. Please choose a number between 1 and 4.")
    
