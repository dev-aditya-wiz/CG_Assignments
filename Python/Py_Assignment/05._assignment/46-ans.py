# Q46
text = input()
middle = len(text) // 2
first = ""
second = ""
for i in range(len(text)):
    if i < middle:
        first += text[i]
    else:
        second += text[i]
print("First Half:", first)
print("Second Half:", second)
