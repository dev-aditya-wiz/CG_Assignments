# Q53
n = int(input())
temp = n
largest = -1
second = -1
for i in range(100):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            second = largest
            largest = digit
        elif digit != largest and digit > second:
            second = digit
        temp //= 10
print(second)
