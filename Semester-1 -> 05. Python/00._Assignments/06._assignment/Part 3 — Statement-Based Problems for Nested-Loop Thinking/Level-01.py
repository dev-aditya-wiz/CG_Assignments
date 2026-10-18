# ================================================ #
# |  Level 1 — Tables and Repeated Calculations  | #
# ================================================ #


# Q96. Multiplication Tables from 1 to N
# Task: Given N and K, print multiplication tables for numbers 1 through N, each from 1 through K.

# Input:
# N = 3
# K = 4

# Expected Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12

N = int(input("Enter N: "))
K = int(input("Enter K: "))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        print(i, "x", j, "=", i * j)


# Q97. Number and Its Divisors
# Task: For every integer from 1 through N, print all of its positive divisors.

# Input: N = 4

# Expected Output:
# 1: 1
# 2: 1 2
# 3: 1 3
# 4: 1 2 4

N = int(input("Enter N: "))

for i in range(1, N + 1):
    print(i, end=": ")

    for j in range(1, i + 1):
        if i % j == 0:
            print(j, end=" ")

    print()


# Q98. Count Divisors for Every Number
# Task: For each number from 1 through N, count its positive divisors.

# Input: N = 5

# Expected Output:
# 1: 1
# 2: 2
# 3: 2
# 4: 3
# 5: 2

N = int(input("Enter N: "))

for i in range(1, N + 1):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    print(i, ":", count)


# Q99. Perfect Numbers in a Range
# Task: Print all perfect numbers from 1 through N.
# A perfect number equals the sum of its positive divisors excluding itself.

# Input: N = 30

# Expected Output:
# 6
# 28

N = int(input("Enter N: "))

for i in range(2, N + 1):
    total = 0

    for j in range(1, i):
        if i % j == 0:
            total += j

    if total == i:
        print(i)


# Q100. Prime Numbers in a Range — Count Each Check
# Task: For each number from 2 through N, determine whether it is prime.
# Print only the prime numbers. Use a nested loop to test possible divisors.

# Input: N = 12

# Expected Output:
# 2 3 5 7 11

N = int(input("Enter N: "))

for i in range(2, N + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end=" ")