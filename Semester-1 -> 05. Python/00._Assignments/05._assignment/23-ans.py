# Q23
n = int(input())
temp = n
count = 0
for i in range(100):
    if temp > 0:
        count += 1
        temp //= 10
print(count)
