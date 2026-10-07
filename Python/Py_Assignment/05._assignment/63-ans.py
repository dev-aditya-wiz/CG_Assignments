# Q63
n = int(input())
total = 0
highest = None
lowest = None
for i in range(n):
    marks = float(input())
    total += marks
    if highest is None or marks > highest:
        highest = marks
    if lowest is None or marks < lowest:
        lowest = marks
average = total / n
print("Total:", int(total) if total.is_integer() else total)
print("Average:", average)
print("Highest:", int(highest) if highest.is_integer() else highest)
print("Lowest:", int(lowest) if lowest.is_integer() else lowest)
