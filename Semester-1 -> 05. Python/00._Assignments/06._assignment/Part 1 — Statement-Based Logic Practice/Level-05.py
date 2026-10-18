# ============================================== #
# | Level 5 — Advanced Shapes and Challenges   | #
# ============================================== #


# Q43. Butterfly Pattern
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = int(input("Enter half-height: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")
    print()


# Q44. Hollow Hourglass
# *********
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *********

n = int(input("Enter half-height: "))

for i in range(n):
    for j in range(i):
        print(" ", end="")

    for j in range(2 * (n - i) - 1):
        if j == 0 or j == 2 * (n - i) - 2 or i == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, n):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q45. Alphabet Diamond
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
#  ABCDCBA
#   ABCBA
#    ABA
#     A

n = int(input("Enter half-height: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i):
        print(chr(65 + j), end="")

    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i):
        print(chr(65 + j), end="")

    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()


# Q46. Pascal's Triangle
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    value = 1

    for j in range(i + 1):
        print(value, end=" ")

        value = value * (i - j) // (j + 1) if j < i else value

    print()


# Q47. Heart Pattern
#  **   **
# **** ****
# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter an odd size (minimum 5): "))

# Top half: two lobes
for i in range(1, (n - 3) // 2 + 1):
    stars = 2 * i

    for j in range((n - stars * 2) // 2):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")

    for j in range(n - 2 * stars):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")
    print()

# Middle row
for j in range(n):
    print("*", end="")
print()

# Bottom half
for i in range(1, (n + 1) // 2):
    stars = n - 2 * i

    for j in range(i):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")
    print()


# Q48. Hollow Heart
#  **   **
# *  * *  *
# *   *   *
#  *     *
#   *   *
#    * *
#     *

n = int(input("Enter an odd size (minimum 5): "))

# Top half
for i in range(1, (n - 3) // 2 + 1):
    stars = 2 * i

    for j in range((n - stars * 2) // 2):
        print(" ", end="")

    print("*", end="")

    for j in range(stars - 2):
        print(" ", end="")

    print("*", end="")

    for j in range(n - 2 * stars):
        print(" ", end="")

    print("*", end="")

    for j in range(stars - 2):
        print(" ", end="")

    print("*")
    
# Lower half
for i in range((n - 3) // 2 + 1):
    for j in range(i):
        print(" ", end="")

    print("*", end="")

    for j in range(n - 2 * i - 3):
        print(" ", end="")

    if i < (n - 3) // 2:
        print("*")
    else:
        print()


# Q49. Star-and-Space Center Pattern
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


# Q50. Custom Symbol Square
# Example input: 4 and #
# ####
# ####
# ####
# ####

n = int(input("Enter size: "))
symbol = input("Enter symbol: ")

for i in range(n):
    for j in range(n):
        print(symbol, end="")
    print()


# Q51. User-Sized Hollow Rectangle
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


# Q52. Create Your Own Pattern
# Example: Alternating Checkerboard
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