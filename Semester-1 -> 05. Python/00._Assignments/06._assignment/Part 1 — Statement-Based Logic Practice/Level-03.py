# ================================================ #
# | Level 3 — Mixed Logic and Repeated Sequences | #
# ================================================ #


# Q24. Increasing and Decreasing Star Triangle
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Q25. Number Hourglass
# 12345
# 1234
# 123
# 12
# 1
# 12
# 123
# 1234
# 12345

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q26. Alphabet Hourglass
# ABCDE
# ABCD
# ABC
# AB
# A
# AB
# ABC
# ABCD
# ABCDE

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

for i in range(2, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# Q27. Alternating Star and Hash Grid
# *#*#*
# #*#*#
# *#*#*
# #*#*#
# *#*#*

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()


# Q28. Binary Checkerboard
# 10101
# 01010
# 10101
# 01010
# 10101

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()


# Q29. Multiplication Grid
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()


# Q30. Alternating-Direction Rows
# 1
# 21
# 123
# 4321
# 12345

n = int(input("Enter size: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        for j in range(i, 0, -1):
            print(j, end="")
    else:
        for j in range(1, i + 1):
            print(j, end="")
    print()


# Q31. Number Diamond
#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1

n = int(input("Enter half-height: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


# Q32. Concentric Number Square
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5

n = int(input("Enter size: "))

for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        top = i
        left = j
        bottom = 2 * n - 2 - i
        right = 2 * n - 2 - j

        minimum = min(top, left, bottom, right)
        print(n - minimum, end=" ")
    print()