# Q29
n = int(input())
temp = n
smallest = 9
for i in range(100):
    if temp > 0:
        digit = temp % 10
        if digit < smallest:
            smallest = digit
        temp //= 10
print(smallest)
