# Q48
text = input()
half = len(text) // 2
equal = True
for i in range(half):
    if text[i] != text[i + half]:
        equal = False
if equal:
    print("Equal Halves")
else:
    print("Different Halves")
