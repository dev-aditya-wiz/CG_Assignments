# Q55
text, target = input().split(", ")
count = 0
total = 0
for char in text:
    total += 1
    if char == target:
        count += 1
frequency = count / total * 100
print("Count =", count, ", Frequency =", f"{frequency:.2f}".rstrip("0").rstrip(".") + "%")
