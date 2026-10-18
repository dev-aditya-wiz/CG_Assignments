# ============================== #
# |  Level 1 — Basic Patterns  | #
# ============================== #

# Q1. Solid Square
# *****
# *****
# *****
# *****
# *****

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()


# Q2. Solid Rectangle
# ******
# ******
# ******

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()


# Q3. Increasing Star Triangle
# *
# **
# ***
# ****
# *****

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


# Q4. Increasing Number Triangle
# 1
# 12
# 123
# 1234
# 12345

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q5. Repeated Number Triangle
# 1
# 22
# 333
# 4444
# 55555

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()


# Q6. Repeated Alphabet Triangle
# A
# BB
# CCC
# DDDD
# EEEEE

n = int(input("Enter size: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end="")
    print()


# Q7. Alphabet Triangle
# A
# AB
# ABC
# ABCD
# ABCDE

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# Q8. Continuous Number Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = int(input("Enter size: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# Q9. Alternating 0–1 Triangle
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n = int(input("Enter size: "))

for i in range(n):
    for j in range(i + 1):
        print((i + j + 1) % 2, end=" ")
    print()


# Q10. Decreasing Star Triangle
# *****
# ****
# ***
# **
# *

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Q11. Decreasing Number Triangle
# 12345
# 1234
# 123
# 12
# 1

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q12. Decreasing Alphabet Triangle
# ABCDE
# ABCD
# ABC
# AB
# A

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()