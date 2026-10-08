#----------------------------#
#-Student Result Information-#
#----------------------------#
name = input()
marks = input().split()
mark1 = int(marks[0])
mark2 = int(marks[1])
mark3 = int(marks[2])
total = mark1 + mark2 + mark3
average = total / 3
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")