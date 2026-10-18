# ============================================ #
# | Level 4 — Hollow Patterns and Conditions | #
# ============================================ #


# Q33. Hollow Square
# *****
# *   *
# *   *
# *   *
# *****

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q34. Hollow Rectangle
# ******
# *    *
# *    *
# ******

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q35. Hollow Number Square
# 11111
# 10001
# 10001
# 10001
# 11111

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("1", end="")
        else:
            print("0", end="")
    print()


# Q36. Hollow Right-Angled Triangle
# *
# **
# * *
# *  *
# *****

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q37. Hollow Inverted Triangle
# *****
# *  *
# * *
# **
# *

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q38. Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if i == n or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q39. Hollow Diamond
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *

n = int(input("Enter half-height: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q40. X Pattern
# *   *
#  * *
#   *
#  * *
# *   *

n = int(input("Enter an odd size: "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q41. Cross Pattern
# *   *
#  * *
# *****
#  * *
# *   *

n = int(input("Enter an odd size: "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q42. Star Cross with Four Arms
# *   *
#  * *
#   *
#  * *
# *   *

n = int(input("Enter an odd size: "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()