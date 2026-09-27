#-------------------------------------------------------#
#------------Q40. Bank Account Verification-------------#
#-------------------------------------------------------#
account_type = input("Enter account type: ")
balance = int(input("Enter balance: "))

if account_type == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")