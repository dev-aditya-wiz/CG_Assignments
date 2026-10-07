# Q52
text = input()
result = ""
for i in range(0, len(text), 2):
    result += text[i + 1] + text[i]
print(result)
