# Q17
n = int(input())
product = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        product *= i
print(product)
