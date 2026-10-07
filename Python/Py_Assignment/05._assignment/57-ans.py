# Q57
n = int(input())
temp = n
even = 0
odd = 0
for i in range(100):
    if temp > 0:
        if (temp % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        temp //= 10
if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")
