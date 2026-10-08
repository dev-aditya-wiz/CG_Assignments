# Q35
n = int(input())
temp = n
position = 1
for i in range(100):
    if temp > 0:
        digit = temp % 10
        print(digit, position)
        position += 1
        temp //= 10
