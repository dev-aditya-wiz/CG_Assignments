# Q34
n = int(input())
temp = n
largest = 0
smallest = 9
for i in range(100):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        temp //= 10
print(largest - smallest)
