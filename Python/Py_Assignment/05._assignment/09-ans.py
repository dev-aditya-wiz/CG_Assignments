# Q9
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        total += i
print(total)
