# Q28
n = int(input())
temp = n
largest = 0
for i in range(100):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        temp //= 10
print(largest)
