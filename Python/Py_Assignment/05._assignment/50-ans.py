# Q50
text = input()
result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i]
print(result)
