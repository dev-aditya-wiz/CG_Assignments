# Q47
text = input()
length = len(text)
first = ""
second = ""
middle = ""
for i in range(length):
    if length % 2 != 0 and i == length // 2:
        middle = text[i]
    elif i < length // 2:
        first += text[i]
    else:
        second += text[i]
if length % 2 != 0:
    print("First Half:", first)
    print("Middle:", middle)
    print("Second Half:", second)
else:
    print("First Half:", first)
    print("Second Half:", second)
