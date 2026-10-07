# Q65
n = int(input())
total = 0
above_10 = 0
for i in range(n):
    units = float(input())
    total += units
    if units > 10:
        above_10 += 1
print("Total Units:", int(total) if total.is_integer() else total)
print("Days Above 10:", above_10)
