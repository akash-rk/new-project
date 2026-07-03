# --- GLOBAL MOCK DATABASE ---
account_database = {
    "holder": "Amit Sharma",
    "balance": 25000
}

# --- YOUR FUNCTIONS GO HERE ---

def show_balance():
     print(account_database)# Write logic to print the name and balance

def deposit(amount):
    # Write logic to add money to the dictionary balance
    pass

def withdraw(amount):
    # Write logic to deduct money safely if funds exist
    pass


# --- THE MAIN SERVER LOOP ---
while True:
    print("\n=== WELCOME TO NEOBANK CORE ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Shutdown Server")
    
    choice = input("Select an option (1-4): ")
    if choice == 1:
        print(f"check Balance {account_database['balance']}")
    elif choice == 2:
        print(f"Deposite money {account_database}")
    # Write your if/elif/else logic here to call the functions
    # Hint: If choice is "2", ask for the deposit amount first, then call deposit(amount)