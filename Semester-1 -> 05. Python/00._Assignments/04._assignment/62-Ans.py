#----------------------------------------------------#
#------------Q62. Shopping Bill Category-------------#
#----------------------------------------------------#
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal >= 5000:
    discount = 20
elif subtotal >= 2000:
    discount = 10
else:
    discount = 0

discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print(f"Subtotal: {subtotal:.0f}")
print(f"Discount: {discount}%")
print(f"Final: {final_amount:.2f}")