# Q56
n = int(input())
temp = n
total = 0
for i in range(100):
    if temp > 0:
        total += temp % 10
        print(total)
        temp //= 10
