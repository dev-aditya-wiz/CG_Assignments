# Q36
n = int(input())
temp = n
total = 0
for i in range(3):
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
