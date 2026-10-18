# ======================================= #
# |  Level 2 — Spaces and Alignment      | #
# ======================================= #


# Q13. Right-Aligned Half Pyramid
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


# Q14. Inverted Right-Aligned Half Pyramid
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


# Q15. Star Pyramid
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


# Q16. Inverted Star Pyramid
# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# Q17. Solid Diamond
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter half-height: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# Q18. Rhombus
#     *****
#    *****
#   *****
#  *****
# *****

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(n):
        print("*", end="")
    print()


# Q19. Mirrored Number Pattern
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()


# Q20. Centered Number Pyramid
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Q21. Palindromic Number Pyramid
#     1
#    121
#   12321
#  1234321
# 123454321

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


# Q22. Alphabet Palindrome Pyramid
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

n = int(input("Enter size: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i):
        print(chr(65 + j), end="")

    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()


# Q23. Reverse-Starting Alphabet Triangle
# E
# D E
# C D E
# B C D E
# A B C D E

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n - i - 1, n):
        print(chr(65 + j), end=" ")
    print()