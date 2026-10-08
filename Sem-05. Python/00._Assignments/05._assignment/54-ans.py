# Q54
text = input()
current = 0
best = 0
previous = ""
for char in text:
    if char == previous:
        current += 1
    else:
        current = 1
        previous = char
    if current > best:
        best = current
print(best)
