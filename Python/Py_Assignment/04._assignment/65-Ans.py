#--------------------------------------------------------#
#------------Q65. Restaurant Ordering System-------------#
#--------------------------------------------------------#
choice = int(input("Enter item number: "))
quantity = int(input("Enter quantity: "))

match choice:
    case 1:
        price = 250
    case 2:
        price = 150
    case 3:
        price = 200
    case 4:
        price = 120
    case _:
        print("Invalid Choice")
        price = 0

total = price * quantity

if total >= 500:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

if price != 0:
    print(f"Total: {total:.0f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final: {final_amount:.2f}")