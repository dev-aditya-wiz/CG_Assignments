# Q33
n = int(input())
temp = n
for i in range(1, 100):
    if temp >= 10:
        temp //= 10
print(temp)
