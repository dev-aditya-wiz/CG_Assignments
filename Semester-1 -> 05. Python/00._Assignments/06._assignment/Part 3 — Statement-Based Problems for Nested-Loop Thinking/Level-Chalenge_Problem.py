# ================================== #
# |  Level 13: Advanced Logic       | #
# ================================== #

# Q121. Print All Pythagorean Triples up to N
# Task: Print all positive integer triples (a, b, c) such that a < b < c,
# a² + b² = c², and c <= N. Print each triple once.

N = int(input("Enter N: "))

for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if a * a + b * b == c * c:
                print(a, b, c)


# ================================== #

# Q122. Find Numbers Equal to the Sum of Their Proper Divisors
# Task: Print all numbers from 2 through N that equal the sum
# of their positive divisors excluding themselves.

N = int(input("Enter N: "))

for number in range(2, N + 1):
    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        print(number)


# ================================== #

# Q123. Print Unique Products in Increasing Factor Order
# Task: For factors from 1 through N, print products i * j where i <= j.
# Print each product only the first time it occurs.
# Do not use lists, sets, or dictionaries.

N = int(input("Enter N: "))

for i in range(1, N + 1):
    for j in range(i, N + 1):
        product = i * j
        already_printed = False

        for previous_i in range(1, N + 1):
            for previous_j in range(previous_i, N + 1):
                previous_product = previous_i * previous_j

                if previous_product == product:
                    if previous_i < i or (
                        previous_i == i and previous_j < j
                    ):
                        already_printed = True

        if not already_printed:
            print(product, end=" ")

print()


# ================================== #

# Q124. Find All Pairs of Prime Numbers with a Given Sum
# Task: Given an even integer N greater than 2, print all pairs
# of prime numbers whose sum is N. Print each pair once.

N = int(input("Enter N: "))

for a in range(2, N // 2 + 1):
    is_prime_a = True

    for divisor in range(2, a):
        if a % divisor == 0:
            is_prime_a = False

    b = N - a
    is_prime_b = True

    if b < 2:
        is_prime_b = False
    else:
        for divisor in range(2, b):
            if b % divisor == 0:
                is_prime_b = False

    if is_prime_a and is_prime_b:
        print(a, b)


# ================================== #

# Q125. Check a Magic-Sum Pattern
# Task: Read an odd integer N and print an N × N addition table
# using row and column numbers. Then print the sum of each row.

N = int(input("Enter an odd integer N: "))

for row in range(1, N + 1):
    for column in range(1, N + 1):
        print(row + column, end=" ")
    print()

print("Row sums:", end=" ")

for row in range(1, N + 1):
    row_sum = 0

    for column in range(1, N + 1):
        row_sum += row + column

    print(row_sum, end=" ")

print()


# ================================== #

# Q126. Count Peaks in a Number Sequence
# Task: Read N integers one by one. Count interior numbers
# strictly greater than both immediate neighbours.
# Use only a few variables, not a list.

N = int(input("Enter N: "))

peaks = 0

if N >= 3:
    previous = int(input("Enter number 1: "))
    current = int(input("Enter number 2: "))

    for position in range(3, N + 1):
        next_number = int(input(f"Enter number {position}: "))

        if current > previous and current > next_number:
            peaks += 1

        previous = current
        current = next_number

print(peaks)


# ================================== #

# Q127. Find Repeated Digit Sums
# Task: Examine every pair of different digit positions in a positive
# integer. Check whether any two different pairs have the same sum.
# Do not use lists or dictionaries.

number = int(input("Enter a positive integer: "))

digits = len(str(number))
repeated = False

for i in range(digits):
    digit_i = (number // (10 ** (digits - 1 - i))) % 10

    for j in range(i + 1, digits):
        digit_j = (number // (10 ** (digits - 1 - j))) % 10
        pair_sum = digit_i + digit_j

        for k in range(digits):
            for m in range(k + 1, digits):
                if k > i or (k == i and m > j):
                    digit_k = (number // (10 ** (digits - 1 - k))) % 10
                    digit_m = (number // (10 ** (digits - 1 - m))) % 10

                    if digit_k + digit_m == pair_sum:
                        repeated = True

if repeated:
    print("Repeated pair sums exist")
else:
    print("No repeated pair sums")


# ================================== #

# Q128. Number Pattern from Row and Column
# Task: Print an N × N grid where each cell contains
# the absolute difference between its one-based row and column numbers.

N = int(input("Enter N: "))

for row in range(1, N + 1):
    for column in range(1, N + 1):
        difference = abs(row - column)
        print(difference, end=" ")
    print()


# ================================== #

# Q129. Compare Digits with Their Neighbours
# Task: Read a positive integer as text. Count digits that are greater
# than both adjacent digits. Ignore the first and last digits.

number = input("Enter a positive integer: ")

peaks = 0

for i in range(1, len(number) - 1):
    previous_digit = int(number[i - 1])
    current_digit = int(number[i])
    next_digit = int(number[i + 1])

    if current_digit > previous_digit and current_digit > next_digit:
        peaks += 1

print(peaks)


# ================================== #

# Q130. Count Increasing Digit Pairs
# Task: Count pairs of digit positions i < j where the digit at
# position i is smaller than the digit at position j.
# Do not convert the number to a list.

number = input("Enter a positive integer: ")

pairs = 0

for i in range(len(number)):
    digit_i = int(number[i])

    for j in range(i + 1, len(number)):
        digit_j = int(number[j])

        if digit_i < digit_j:
            pairs += 1

print(pairs)


# ================================== #

# Q131. Character Frequency Compression Without a Dictionary
# Task: Print each distinct character followed by its frequency,
# in the order of its first appearance.
# Do not use a dictionary, count(), or lists.

s = input("Enter a string: ")

for i in range(len(s)):
    already_seen = False

    for j in range(i):
        if s[i] == s[j]:
            already_seen = True

    if not already_seen:
        frequency = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                frequency += 1

        print(s[i], frequency, sep="", end="")

print()