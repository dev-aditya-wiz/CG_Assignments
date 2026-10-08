# Q49
text = input()
symmetric = True
for i in range(len(text)):
    if text[i] != text[len(text) - 1 - i]:
        symmetric = False
if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")
