correct_pin = 1234
balance = 5000  # initial balance

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("Login successful!")
    print("Your balance is:", balance)

    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient funds!")
else:
    print("Incorrect PIN!")