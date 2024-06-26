import random

accounts = {}

def create_account(user_id, initial_balance):
    if user_id in accounts:
        print("User ID already exists! Please choose a different User ID.")
    else:
        accounts[user_id] = initial_balance
        print(f"Account created successfully! User ID: {user_id}, Balance: {initial_balance}")

def check_balance(user_id):
    if user_id in accounts:
        print(f"Your Balance: {accounts[user_id]}")
    else:
        print("User ID not found!")

def deposit(user_id, amount):
    if user_id in accounts:
        accounts[user_id] += amount
        print(f"Deposited {amount}")
    else:
        print("User ID not found!")

def withdraw(user_id, amount):
    if user_id in accounts:
        if accounts[user_id] >= amount:
            accounts[user_id] -= amount
            print(f"Withdraw {amount}")
        else:
            print("Insufficient funds!")
    else:
        print("User ID not found!")

def delete_account(user_id):
    if user_id in accounts:
        del accounts[user_id]
        print(f"Account with User ID {user_id} deleted.")
    else:
        print("User ID not found!")

def main():
    while True:
        print("\nWelcome to ACLC Bank")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter User ID: ")
            initial_balance = float(input("Enter initial balance: "))
            create_account(user_id, initial_balance)
        elif choice == '2':
            user_id = input("Enter User ID: ")
            check_balance(user_id)
        elif choice == '3':
            user_id = input("Enter User ID: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(user_id, amount)
        elif choice == '4':
            user_id = input("Enter User ID: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(user_id, amount)
        elif choice == '5':
            user_id = input("Enter User ID: ")
            delete_account(user_id)
        elif choice == '6':
            print("Thank you for using My Bank!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
