#-----------------------------------------------------#
#-----------------Q38. ATM Withdrawal-----------------#
#-----------------------------------------------------#
balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")