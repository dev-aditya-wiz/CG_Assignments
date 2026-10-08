# Q18
n = int(input())
product = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        product *= i
print(product)
