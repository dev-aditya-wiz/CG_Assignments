# ========================================== #
# | Level 2 — Compare Items and Find Pairs |
# ========================================== #


# Q101. Pairs of Digits with a Target Sum
# Task: Given a positive integer, examine every pair of its digits in their original order.
# Print pairs whose sum equals the target. Do not pair a digit with itself.

# Input:
# number = 12345
# target = 6

# Expected Output:
# 1 5
# 2 4

number = input("Enter a number: ")
target = int(input("Enter target sum: "))

for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if int(number[i]) + int(number[j]) == target:
            print(number[i], number[j])


# Q102. Digit Pairs with a Fixed Difference
# Task: Given a positive integer, print every pair of digits whose absolute difference equals D.
# Keep the digits in the order they appear in the number.

# Input:
# number = 14253
# D = 2

# Expected Output:
# 1 3
# 4 2
# 2 5
# 5 3

number = input("Enter a number: ")
D = int(input("Enter difference: "))

for i in range(len(number)):
    for j in range(i + 1, len(number)):
        difference = abs(int(number[i]) - int(number[j]))

        if difference == D:
            print(number[i], number[j])


# Q103. Repeated Digits in a Number
# Task: Print each digit that appears more than once, only once,
# in the order of its first appearance. Do not use a list, set, or dictionary.

# Input: number = 4243124

# Expected Output:
# 4
# 2

number = input("Enter a number: ")

for i in range(len(number)):
    appeared_before = False

    for k in range(i):
        if number[i] == number[k]:
            appeared_before = True
            break

    if not appeared_before:
        count = 0

        for j in range(len(number)):
            if number[i] == number[j]:
                count += 1

        if count > 1:
            print(number[i])


# Q104. Count Equal Digit Pairs
# Task: Count pairs of different digit positions that contain the same digit.

# Input: number = 12131

# Expected Output: 4

number = input("Enter a number: ")

count = 0

for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] == number[j]:
            count += 1

print(count)


# Q105. Common Characters in Two Strings
# Task: Given two strings, print each character that occurs in both strings, only once,
# in the order it first appears in the first string. Do not use a set or dictionary.

# Input:
# first = "program"
# second = "grammar"

# Expected Output:
# r
# g
# a
# m

first = input("Enter first string: ")
second = input("Enter second string: ")

for i in range(len(first)):
    appeared_before = False

    for k in range(i):
        if first[i] == first[k]:
            appeared_before = True
            break

    if not appeared_before:
        for j in range(len(second)):
            if first[i] == second[j]:
                print(first[i])
                break


# Q106. Check Whether Two Strings Share a Character
# Task: Print True if two strings have at least one character in common;
# otherwise print False. Use nested loops to compare characters.

# Test Case 1
# Input:
# first = "cat"
# second = "dog"
# Expected Output: False

# Test Case 2
# Input:
# first = "python"
# second = "phone"
# Expected Output: True

first = input("Enter first string: ")
second = input("Enter second string: ")

found = False

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            found = True
            break

    if found:
        break

print(found)


# Q107. Seating Plan
# Task: Read the number of rows and seats per row.
# Print seat labels row by row, starting from seat 1 in each row.

# Input:
# rows = 3
# seats_per_row = 4

# Expected Output:
# Row 1: 1 2 3 4
# Row 2: 1 2 3 4
# Row 3: 1 2 3 4

rows = int(input("Enter number of rows: "))
seats_per_row = int(input("Enter seats per row: "))

for i in range(1, rows + 1):
    print("Row", i, end=": ")

    for j in range(1, seats_per_row + 1):
        print(j, end=" ")

    print()


# Q108. Student Marks and Class Total
# Task: Read the marks of S students in T tests one value at a time.
# Print each student's total and the class total.
# Do not store the marks in a list.

# Input:
# Students = 3
# Tests = 2
# Marks in order: 10, 20, 15, 15, 20, 10

# Expected Output:
# Student 1 total: 30
# Student 2 total: 30
# Student 3 total: 30
# Class total: 90

students = int(input("Enter number of students: "))
tests = int(input("Enter number of tests: "))

class_total = 0

for i in range(1, students + 1):
    student_total = 0

    for j in range(1, tests + 1):
        marks = int(input("Enter marks: "))
        student_total += marks

    print("Student", i, "total:", student_total)
    class_total += student_total

print("Class total:", class_total)


# Q109. Daily Rainfall Summary
# Task: Read rainfall measurements for D days and S stations one value at a time.
# Print the total rainfall for each day. Do not store the measurements in a list.

# Input:
# Days = 2
# Stations = 3
# Measurements in order: 2, 0, 5, 1, 4, 3

# Expected Output:
# Day 1 total: 7
# Day 2 total: 8

days = int(input("Enter number of days: "))
stations = int(input("Enter number of stations: "))

for i in range(1, days + 1):
    daily_total = 0

    for j in range(1, stations + 1):
        rainfall = int(input("Enter rainfall: "))
        daily_total += rainfall

    print("Day", i, "total:", daily_total)


# Q110. Largest of Several Numbers in Each Group
# Task: Read G groups with K numbers per group.
# For each group, print its largest number.
# Do not store the group in a list.

# Input:
# Groups = 2
# Numbers per group = 3
# Numbers in order: 4, 9, 2, 7, 1, 5

# Expected Output:
# 9
# 7

groups = int(input("Enter number of groups: "))
K = int(input("Enter numbers per group: "))

for i in range(1, groups + 1):
    largest = int(input("Enter a number: "))

    for j in range(1, K):
        number = int(input("Enter a number: "))

        if number > largest:
            largest = number
    print(largest)


# Q111. Sum of Numbers by Group and Position
# Task: Read two groups of three numbers.
# Print the sum of each group, then the sum of each position across the groups.
# Do not store the numbers in a list.

# Input:
# Group 1: 1, 2, 3
# Group 2: 4, 5, 6

# Expected Output:
# Group sums: 6 15
# Position sums: 5 7 9

group1_sum = 0
group2_sum = 0

position1 = 0
position2 = 0
position3 = 0

for group in range(1, 3):
    group_sum = 0

    for position in range(1, 4):
        number = int(input("Enter a number: "))
        group_sum += number

        if position == 1:
            position1 += number
        elif position == 2:
            position2 += number
        else:
            position3 += number

    if group == 1:
        group1_sum = group_sum
    else:
        group2_sum = group_sum

print("Group sums:", group1_sum, group2_sum)
print("Position sums:", position1, position2, position3)


# Q112. Number Pair Comparison Table
# Task: Print an N × N table where each cell contains the sum of its row and column numbers.

# Input: N = 3

# Expected Output:
# 2 3 4
# 3 4 5
# 4 5 6

N = int(input("Enter N: "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(i + j, end=" ")

    print()


# Q113. Count Zeroes in a Number Sequence
# Task: Read N integers one at a time and count how many are zero.
# Do not store the numbers in a list.

# Input:
# N = 6
# Numbers: 0, 2, 0, 3, 0, 4

# Expected Output: 3

N = int(input("Enter N: "))

count = 0

for i in range(N):
    number = int(input("Enter a number: "))

    if number == 0:
        count += 1

print(count)


# Q114. Print Row and Column Coordinates
# Task: Read R and C. Print each coordinate using row and column numbers starting from zero.
# Do not use a list or matrix.

# Input:
# R = 2
# C = 3

# Expected Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)

R = int(input("Enter number of rows: "))
C = int(input("Enter number of columns: "))

for i in range(R):
    for j in range(C):
        print("(", i, ",", j, ")", end=" ")

    print()


# Q115. Find Every Occurrence of a Substring
# Task: Given a text and a short pattern, print every starting index where the pattern occurs.
# Overlapping matches must be included. Do not use str.find() or str.count().

# Input:
# text = "aaaa"
# pattern = "aa"

# Expected Output:
# 0 1 2

text = input("Enter text: ")
pattern = input("Enter pattern: ")

for i in range(len(text) - len(pattern) + 1):
    match = True

    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break

    if match:
        print(i, end=" ")


# Q116. Count Matching Character Pairs
# Task: Count pairs of positions i < j in a string that contain the same character.

# Input: s = "abca"

# Expected Output: 1

s = input("Enter a string: ")

count = 0

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count += 1

print(count)


# Q117. Check Whether Two Strings Are Anagrams
# Task: Check whether two strings contain the same characters with the same frequencies.
# Uppercase and lowercase are different. Assume there are no spaces.

# Test Case 1
# Input:
# first = "listen"
# second = "silent"
# Expected Output: True

# Test Case 2
# Input:
# first = "hello"
# second = "world"
# Expected Output: False

first = input("Enter first string: ")
second = input("Enter second string: ")

is_anagram = True

if len(first) != len(second):
    is_anagram = False
else:
    for i in range(len(first)):
        count_first = 0
        count_second = 0

        for j in range(len(first)):
            if first[i] == first[j]:
                count_first += 1

            if first[i] == second[j]:
                count_second += 1

        if count_first != count_second:
            is_anagram = False
            break

print(is_anagram)


# Q118. Print Character Frequency Without a Dictionary
# Task: Print each distinct character and its frequency in order of first appearance.
# Do not use a dictionary or count().

# Input: s = "banana"

# Expected Output:
# b: 1
# a: 3
# n: 2

s = input("Enter a string: ")

for i in range(len(s)):
    appeared_before = False

    for k in range(i):
        if s[i] == s[k]:
            appeared_before = True
            break

    if not appeared_before:
        count = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1

        print(s[i] + ":", count)


# Q119. Find Repeated Adjacent Characters
# Task: Print every character that appears in two or more consecutive positions,
# along with the number of times it repeats in that consecutive group.

# Input: s = "aaabbccccdaa"

# Expected Output:
# a: 3
# b: 2
# c: 4
# a: 2

s = input("Enter a string: ")

i = 0

while i < len(s):
    count = 1
    j = i + 1

    while j < len(s) and s[j] == s[i]:
        count += 1
        j += 1

    if count >= 2:
        print(s[i] + ":", count)

    i = j


# Q120. Compare Two Words Position by Position
# Task: Given two strings of equal length, count how many positions contain different characters.

# Input:
# first = "house"
# second = "mouse"

# Expected Output: 1

first = input("Enter first string: ")
second = input("Enter second string: ")

count = 0

for i in range(len(first)):
    if first[i] != second[i]:
        count += 1

print(count)