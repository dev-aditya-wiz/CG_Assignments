# Q30
n = int(input())
temp = n
reverse = 0
for i in range(100):
    if temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10
print(reverse)
