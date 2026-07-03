database_record = {
    "account_holder": "Amit Sharma",
    "account_age_months": 2,     
    "account_balance": 50000    
}

while True:
           if database_record["account_balance"] == 0:
                  break
           command = input("Enter command('continue' or 'exit'): ")
           if command == 'exit':
                  break
           if command == 'continue':
                  transaction_amount = int(input("Enter transaction amount (₹): "))

                  if transaction_amount > database_record["account_balance"]:
                    print("Transaction Status: DECLINED \nReason: Insufficient funds in account.")
                  elif  database_record["account_age_months"] <= 3 and transaction_amount > 20000:
                     print("Transaction Status: FLAGGED FOR REVIEW \nReason: High-value transaction on a new account. Funds are on hold.")
                  else:
                    print("Transaction Status: APPROVED \nProcessing payment...")
                    database_record["account_balance"] = database_record["account_balance"] - transaction_amount
                    print(f"Bank balance:₹{database_record['account_balance']}")