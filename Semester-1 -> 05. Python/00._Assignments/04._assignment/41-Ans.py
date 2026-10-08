#---------------------------------------------------------#
#------------Q41. Online Shopping Eligibility-------------#
#---------------------------------------------------------#
amount = int(input("Enter order amount: "))
payment = input("Enter payment method: ")

if amount >= 500:
    if payment == "card":
        print("Card Payment Accepted")
    elif payment == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")