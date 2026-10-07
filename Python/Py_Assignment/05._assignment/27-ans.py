# Q27
n = int(input())
temp = n
total = 0
for i in range(100):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            total += digit
        temp //= 10
print(total)
