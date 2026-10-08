# Q62
n = int(input())
total = 0
highest = None
lowest = None
for i in range(n):
    expense = float(input())
    total += expense
    if highest is None or expense > highest:
        highest = expense
    if lowest is None or expense < lowest:
        lowest = expense
print("Total:", int(total) if total.is_integer() else total)
print("Highest:", int(highest) if highest.is_integer() else highest)
print("Lowest:", int(lowest) if lowest.is_integer() else lowest)
