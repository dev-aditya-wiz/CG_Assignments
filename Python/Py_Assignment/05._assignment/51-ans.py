# Q51
text = input()
even = 0
odd = 0
for i in range(len(text)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Index =", even, "Odd Index =", odd)
