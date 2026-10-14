# ========================================== #
# | Level 2 — Compare Items and Find Pairs | #
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



# Q103. Repeated Digits in a Number
# Task: Print each digit that appears more than once, only once, in the order of its first appearance. 
# Do not convert the number into a list or use a set/dictionary.

# Input: number = 4243124

# Expected Output:

# 4
# 2
# Q104. Count Equal Digit Pairs
# Task: Count pairs of different digit positions that contain the same digit.

# Test Case 1

# Input: number = 12131

# Expected Output: 4

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



# Q106. Check Whether Two Strings Share a Character
# Task: Print True if two strings have at least one character in common; otherwise print False. 
# Use nested loops to compare characters.

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



# Q108. Student Marks and Class Total
# Task: Read the marks of S students in T tests one value at a time. 
# Print each student's total and the class total. 
# Do not store the marks in a list; accumulate totals as the values are read.

# Input:
# Students = 3
# Tests = 2
# Marks in order: 10, 20, 15, 15, 20, 10

# Expected Output:
# Student 1 total: 30
# Student 2 total: 30
# Student 3 total: 30
# Class total: 90



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



# Q110. Largest of Several Numbers in Each Group
# Task: Read G groups with K numbers per group. For each group, print its largest number. Read each number individually and do not store the group in a list.

# Input:
# Groups = 2
# Numbers per group = 3
# Numbers in order: 4, 9, 2, 7, 1, 5

# Expected Output:
# 9
# 7



# Q111. Sum of Numbers by Group and Position
# Task: Read two groups of three numbers. 
# Print the sum of each group, 
# then print the sum of the first, second, 
# and third positions across the groups. 
# Do not store the numbers in a list.

# Input:
# Group 1: 1, 2, 3
# Group 2: 4, 5, 6

# Expected Output:
# Group sums: 6 15
# Position sums: 5 7 9



# Q112. Number Pair Comparison Table
# Task: Read an integer N. Print an N × N table where each cell contains 
# the sum of its row number and column number, both starting from 1.

# Input: N = 3

# Expected Output:
# 2 3 4
# 3 4 5
# 4 5 6



# Q113. Count Zeroes in a Number Sequence
# Task: Read N integers one at a time and count how many are zero. Do not store the numbers in a list.

# Input:
# N = 6
# Numbers: 0, 2, 0, 3, 0, 4
# Expected Output: 3



# Q114. Print Row and Column Coordinates
# Task: Read R and C. Print each coordinate using row and column numbers starting from zero. 
# This question focuses on nested-loop counting; do not use a list or matrix.

# Input:
# R = 2
# C = 3

# Expected Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)



# Q115. Find Every Occurrence of a Substring
# Task: Given a text and a short pattern, print every starting index where the pattern occurs. 
# Overlapping matches must be included. Do not use str.find() or str.count().

# Input:
# text = "aaaa"
# pattern = "aa"
# Expected Output:
# 0 1 2



# Q116. Count Matching Character Pairs
# Task: Count pairs of positions i < j in a string that contain the same character.

# Input: s = "abca"
# Expected Output: 1



# Q117. Check Whether Two Strings Are Anagrams
# Task: Check whether two strings contain the same characters with the same frequencies. 
# Treat uppercase and lowercase as different, and assume there are no spaces.

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



# Q118. Print Character Frequency Without a Dictionary
# Task: Print each distinct character and its frequency in the order of its first appearance. Do not use a dictionary or count().

# Input: s = "banana"

# Expected Output:
# b: 1
# a: 3
# n: 2



# Q119. Find Repeated Adjacent Characters
# Task: Print every character that appears in two or more consecutive positions, along with the number of times it repeats in that consecutive group.

# Input: s = "aaabbccccdaa"

# Expected Output:
# a: 3
# b: 2
# c: 4
# a: 2



# Q120. Compare Two Words Position by Position
# Task: Given two strings of equal length, count how many positions contain different characters.

# Input:
# first = "house"
# second = "mouse"

# Expected Output: 1

