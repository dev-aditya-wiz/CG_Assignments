#------------------------------------------------#
#------------Q35. Secure Transaction-------------#
#------------------------------------------------#
amount = int(input("Enter amount: "))
otp = input("Enter OTP: ")

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")