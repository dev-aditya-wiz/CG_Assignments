# Q66
n = int(input())
total = 0
above_1000 = 0
for i in range(n):
    price = float(input())
    total += price
    if price > 1000:
        above_1000 += 1
print("Total Bill:", int(total) if total.is_integer() else total)
print("Products Above 1000:", above_1000)
