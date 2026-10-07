# Q25
n = int(input())
temp = n
product = 1
for i in range(100):
    if temp > 0:
        product *= temp % 10
        temp //= 10
print(product)
