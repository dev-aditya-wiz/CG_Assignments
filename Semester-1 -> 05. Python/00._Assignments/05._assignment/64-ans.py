# Q64
n = int(input())
present = 0
absent = 0
for i in range(n):
    status = input().strip().upper()
    if status == "P":
        present += 1
    elif status == "A":
        absent += 1
attendance = present / n * 100
print("Present:", present)
print("Absent:", absent)
print(f"Attendance: {attendance:.2f}%")
