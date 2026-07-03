# --- GLOBAL MOCK DATABASE ---
account_database = {
    "holder": "Amit Sharma",
    "balance": 25000
}



def show_balance():
     print(account_database)

def deposit(amount):
    
    pass

def withdraw(amount):
    
    pass

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
    
