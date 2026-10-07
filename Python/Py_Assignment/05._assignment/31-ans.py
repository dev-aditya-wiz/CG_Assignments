# Q31
n = int(input())
original = n
temp = n
reverse = 0
for i in range(100):
    if temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
