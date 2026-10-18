# ================================== #
# |  Level 1 — Basic Number Logic  | #
# ================================== #


# Q66. Count Digits

# Task: Count the digits in an integer. Ignore its sign. Zero has one digit.
# Test Case: Input: n = 0 → Expected Output: 1
# Test Case: Input: n = 1234 → Expected Output: 4
# Test Case: Input: n = -98 → Expected Output: 2

n = int(input("Enter a number: "))
n = abs(n)

count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print(count)


# Q67. Sum of Digits

# Task: Find the sum of a number's digits.
# Test Case: Input: n = 123 → Expected Output: 6
# Test Case: Input: n = 505 → Expected Output: 10
# Test Case: Input: n = 9 → Expected Output: 9

n = int(input("Enter a number: "))
n = abs(n)

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)


# Q68. Product of Digits

# Task: Find the product of a number's digits.
# Test Case: Input: n = 123 → Expected Output: 6
# Test Case: Input: n = 505 → Expected Output: 0
# Test Case: Input: n = 46 → Expected Output: 24

n = int(input("Enter a number: "))
n = abs(n)

product = 1

if n == 0:
    product = 0
else:
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10

print(product)


# Q69. Reverse a Number

# Task: Print the digits of a number in reverse order. Leading zeroes in the result are dropped.
# Test Case: Input: n = 1234 → Expected Output: 4321
# Test Case: Input: n = 100 → Expected Output: 1
# Test Case: Input: n = 507 → Expected Output: 705

n = int(input("Enter a number: "))

sign = -1 if n < 0 else 1
n = abs(n)

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse * sign)


# Q70. Palindrome Number

# Task: Check whether a number reads the same forwards and backwards.
# Test Case: Input: n = 121 → Expected Output: True
# Test Case: Input: n = 123 → Expected Output: False
# Test Case: Input: n = 0 → Expected Output: True

n = int(input("Enter a number: "))

original = n
temp = abs(n)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if n >= 0 and original == reverse:
    print(True)
else:
    print(False)


# Q71. Prime Number

# Task: Check whether a number is prime. Numbers less than 2 are not prime.
# Test Case: Input: n = 2 → Expected Output: True
# Test Case: Input: n = 17 → Expected Output: True
# Test Case: Input: n = 15 → Expected Output: False

n = int(input("Enter a number: "))

is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print(is_prime)


# Q72. Primes from 1 to N

# Task: Print every prime number from 1 through N.
# Test Case: Input: N = 10 → Expected Output: 2 3 5 7
# Test Case: Input: N = 5 → Expected Output: 2 3 5
# Test Case: Input: N = 2 → Expected Output: 2

N = int(input("Enter N: "))

for i in range(2, N + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end=" ")


# Q73. First N Fibonacci Numbers

# Task: Print the first N Fibonacci numbers, starting with 0, 1, 1, 2, 3, ....
# Test Case: Input: N = 5 → Expected Output: 0 1 1 2 3
# Test Case: Input: N = 1 → Expected Output: 0
# Test Case: Input: N = 7 → Expected Output: 0 1 1 2 3 5 8

N = int(input("Enter N: "))

a = 0
b = 1

for i in range(N):
    print(a, end=" ")

    next_number = a + b
    a = b
    b = next_number


# Q74. GCD of Two Numbers

# Task: Find the greatest common divisor (GCD) of two positive integers using a loop.
# Test Case: Input: a = 12, b = 18 → Expected Output: 6
# Test Case: Input: a = 5, b = 9 → Expected Output: 1
# Test Case: Input: a = 20, b = 100 → Expected Output: 20

a = int(input("Enter a: "))
b = int(input("Enter b: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)


# Q75. LCM of Two Numbers

# Task: Find the least common multiple (LCM) of two positive integers.
# Test Case: Input: a = 4, b = 6 → Expected Output: 12
# Test Case: Input: a = 5, b = 7 → Expected Output: 35
# Test Case: Input: a = 3, b = 9 → Expected Output: 9

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break