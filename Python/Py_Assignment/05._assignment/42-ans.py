# Q42
text = input()
upper = 0
lower = 0
for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("Uppercase =", upper, "Lowercase =", lower)
