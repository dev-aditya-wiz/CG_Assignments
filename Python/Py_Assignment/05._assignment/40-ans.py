# Q40
text = input()
target = input()
count = 0
for char in text:
    if char == target:
        count += 1
print(count)
