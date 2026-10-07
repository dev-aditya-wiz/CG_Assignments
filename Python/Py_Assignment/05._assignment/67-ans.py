# Q67
n = int(input())
successful = 0
failed = 0
for i in range(n):
    attempt = input().strip().lower()
    if attempt == "success":
        successful += 1
    elif attempt == "failed":
        failed += 1
rate = successful / n * 100
print("Successful:", successful)
print("Failed:", failed)
print("Success Rate:", f"{rate:.2f}".rstrip("0").rstrip(".") + "%")
