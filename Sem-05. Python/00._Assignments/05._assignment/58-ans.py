# Q58
n = int(input())
temp = n
total = 0
sign = 1
for i in range(100):
    if temp > 0:
        digit = temp % 10
        total += sign * digit
        sign *= -1
        temp //= 10
print(total)
