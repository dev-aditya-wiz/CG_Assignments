#-----------------------------------------------------#
#--------------------Q64. ATM Menu--------------------#
#-----------------------------------------------------#
balance = 10000

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print(f"Balance: {balance}")

    case 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print(f"Deposit Successful, Balance: {balance}")

    case 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print(f"Withdrawal Successful, Balance: {balance}")
        else:
            print("Insufficient Balance")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")