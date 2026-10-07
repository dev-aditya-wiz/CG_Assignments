# Q32
n, target = map(int, input().split())
temp = n
count = 0
for i in range(100):
    if temp > 0:
        if temp % 10 == target:
            count += 1
        temp //= 10
print(count)
