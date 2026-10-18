# ======================================= #
# | Level 6 — Additional Patterns       | #
# ======================================= #


# Q53. Number Increasing Reverse Pyramid
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Q54. Square Fill Pattern
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# Q55. Left Half Pyramid
#     *
#    ***
#   *****
#  *******
# *********

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")
    print()


# Q56. Reverse Right Half Pyramid
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


# Q57. Left Half Pyramid — Increasing
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


# Q58. Reverse Left Half Pyramid
# *****
#  ****
#   ***
#    **
#     *

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    print()


# Q59. Triangle Star Pattern
#     *
#    **
#   ***
#  ****
# *****

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    print()


# Q60. Mirror-Image Number Triangle
# 1 2 3 4
#  2 3 4
#   3 4
#    4

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i - 1):
        print(" ", end="")

    for j in range(i, n + 1):
        print(j, end=" ")

    print()


# Q61. Hollow Reverse Triangle
# *****
#  *  *
#   * *
#    **
#     *

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(i - 1):
        print(" ", end="")

    for j in range(n - i + 1):
        if i == 1 or j == 0 or j == n - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q62. Hollow Diamond Pyramid
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

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q63. Hollow Hourglass Pattern
# *       *
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *       *

n = int(input("Enter half-height: "))

for i in range(n):
    for j in range(i):
        print(" ", end="")

    for j in range(2 * (n - i) - 1):
        if j == 0 or j == 2 * (n - i) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, n):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q64. Right Pascal's Triangle
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


# Q65. Pattern Size Challenge
# Test your pattern with N = 3, N = 5, and N = 7.

for n in (3, 5, 7):
    print("Pattern size:", n)

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("*", end="")
            else:
                print("#", end="")
        print()

    print()