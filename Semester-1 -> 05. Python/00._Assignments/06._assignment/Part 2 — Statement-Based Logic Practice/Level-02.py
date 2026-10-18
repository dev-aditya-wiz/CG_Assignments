# ================================== #
# |  Level 2 — Basic String Logic  | #
# ================================== #
# Task: Assume string comparisons are case-sensitive unless the question says otherwise.


# Q76. Length of a String

# Task: Print the number of characters in a string.
# Test Case: Input: s = "hello" → Expected Output: 5
# Test Case: Input: s = "" → Expected Output: 0
# Test Case: Input: s = "Python" → Expected Output: 6

s = input("Enter a string: ")

count = 0

for ch in s:
    count += 1

print(count)


# Q77. Print Each Character

# Task: Print each character of a string on a separate line.
# Test Case: Input: s = "cat" → Expected Output: c, a, t on separate lines
# Test Case: Input: s = "hi" → Expected Output: h, i on separate lines

s = input("Enter a string: ")

for ch in s:
    print(ch)


# Q78. Count Vowels

# Task: Count a, e, i, o, and u. Count uppercase vowels too.
# Test Case: Input: s = "hello" → Expected Output: 2
# Test Case: Input: s = "JAVASCRIPT" → Expected Output: 3
# Test Case: Input: s = "sky" → Expected Output: 0

s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print(count)


# Q79. Count Consonants

# Task: Count English letters that are not vowels. Ignore spaces, digits, and punctuation.
# Test Case: Input: s = "hello" → Expected Output: 3
# Test Case: Input: s = "abc" → Expected Output: 2
# Test Case: Input: s = "a e i" → Expected Output: 0

s = input("Enter a string: ")

count = 0

for ch in s:
    if ch.isalpha() and ch.isascii() and ch not in "aeiouAEIOU":
        count += 1

print(count)


# Q80. Convert to Uppercase

# Task: Convert all lowercase letters to uppercase.
# Test Case: Input: s = "hello" → Expected Output: "HELLO"
# Test Case: Input: s = "Js" → Expected Output: "JS"
# Test Case: Input: s = "123abc" → Expected Output: "123ABC"

s = input("Enter a string: ")

result = ""

for ch in s:
    if "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)


# Q81. Convert to Lowercase

# Task: Convert all uppercase letters to lowercase.
# Test Case: Input: s = "HELLO" → Expected Output: "hello"
# Test Case: Input: s = "Js" → Expected Output: "js"
# Test Case: Input: s = "123ABC" → Expected Output: "123abc"

s = input("Enter a string: ")

result = ""

for ch in s:
    if "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)


# Q82. Reverse a String

# Task: Print the characters in reverse order.
# Test Case: Input: s = "hello" → Expected Output: "olleh"
# Test Case: Input: s = "abc" → Expected Output: "cba"
# Test Case: Input: s = "a" → Expected Output: "a"

s = input("Enter a string: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

print(reverse)


# Q83. Palindrome String

# Task: Check whether a string reads the same forwards and backwards.
# Test Case: Input: s = "madam" → Expected Output: True
# Test Case: Input: s = "racecar" → Expected Output: True
# Test Case: Input: s = "hello" → Expected Output: False

s = input("Enter a string: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

if s == reverse:
    print(True)
else:
    print(False)


# Q84. Count a Specific Character

# Task: Count how many times the character a or A appears.
# Test Case: Input: s = "banana" → Expected Output: 3
# Test Case: Input: s = "Apple" → Expected Output: 1
# Test Case: Input: s = "xyz" → Expected Output: 0

s = input("Enter a string: ")

count = 0

for ch in s:
    if ch == "a" or ch == "A":
        count += 1

print(count)


# Q85. Remove All Spaces

# Task: Remove space characters from a string.
# Test Case: Input: s = "hello world" → Expected Output: "helloworld"
# Test Case: Input: s = "a b c" → Expected Output: "abc"
# Test Case: Input: s = "no_spaces" → Expected Output: "no_spaces"

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)