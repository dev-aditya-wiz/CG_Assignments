#---------------------------------------------------------#
#------------Q48. Product Purchase Validation-------------#
#---------------------------------------------------------#
stock = int(input("Enter stock: "))
payment = input("Enter payment status: ")

if stock > 0:
    if payment == "paid":
        print("Order Confirmed")
    elif payment == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")