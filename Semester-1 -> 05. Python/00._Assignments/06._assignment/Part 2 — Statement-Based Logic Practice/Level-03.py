# ========================================== #
# |     Level 3 — More String Practice     | #
# ========================================== #


# Q86. Count Words
# Task: Count the words in a sentence. Ignore extra spaces at the beginning, end, or between words.
# Test Case: Input: s = "Hello world" → Expected Output: 2
# Test Case: Input: s = "Python is fun" → Expected Output: 3
# Test Case: Input: s = "  this   is spaced  " → Expected Output: 3

s = input("Enter a sentence: ")

count = 0
inside_word = False

for ch in s:
    if ch != " ":
        if not inside_word:
            count += 1
            inside_word = True
    else:
        inside_word = False

print(count)


# Q87. Replace All 'a' with 'e'
# Task: Replace every lowercase a with e.
# Test Case: Input: s = "banana" → Expected Output: "benene"
# Test Case: Input: s = "apple" → Expected Output: "epple"
# Test Case: Input: s = "cat" → Expected Output: "cet"

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == "a":
        result += "e"
    else:
        result += ch

print(result)


# Q88. Check for a Character
# Task: Check whether a given character occurs in a string.
# Test Case: Input: s = "hello", ch = "e" → Expected Output: True
# Test Case: Input: s = "hello", ch = "a" → Expected Output: False
# Test Case: Input: s = "JavaScript", ch = "S" → Expected Output: False

s = input("Enter a string: ")
ch = input("Enter a character: ")

found = False

for char in s:
    if char == ch:
        found = True
        break

print(found)


# Q89. Compare Two Strings
# Task: Check whether two strings are exactly equal, including letter case and spaces.
# Test Case: Input: "hello", "hello" → Expected Output: True
# Test Case: Input: "Hello", "hello" → Expected Output: False
# Test Case: Input: "js", "js " → Expected Output: False

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print(True)
else:
    print(False)


# Q90. Count Digits in a String
# Task: Count the characters that are digits from 0 to 9.
# Test Case: Input: s = "abc123" → Expected Output: 3
# Test Case: Input: s = "2025 year" → Expected Output: 4
# Test Case: Input: s = "no digits" → Expected Output: 0

s = input("Enter a string: ")

count = 0

for ch in s:
    if "0" <= ch <= "9":
        count += 1

print(count)


# Q91. Count Uppercase Letters
# Task: Count uppercase English letters.
# Test Case: Input: s = "HeLLo" → Expected Output: 3
# Test Case: Input: s = "javascript" → Expected Output: 0
# Test Case: Input: s = "JS 101" → Expected Output: 2

s = input("Enter a string: ")

count = 0

for ch in s:
    if "A" <= ch <= "Z":
        count += 1

print(count)


# Q92. Count Lowercase Letters
# Task: Count lowercase English letters.
# Test Case: Input: s = "HeLLo" → Expected Output: 2
# Test Case: Input: s = "JAVASCRIPT" → Expected Output: 0
# Test Case: Input: s = "Js 101" → Expected Output: 1

s = input("Enter a string: ")

count = 0

for ch in s:
    if "a" <= ch <= "z":
        count += 1

print(count)


# Q93. Remove All Vowels
# Task: Remove all vowels, including uppercase vowels.
# Test Case: Input: s = "hello" → Expected Output: "hll"
# Test Case: Input: s = "JavaScript" → Expected Output: "JvScrpt"
# Test Case: Input: s = "AEIOU" → Expected Output: ""

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in "aeiouAEIOU":
        result += ch

print(result)


# Q94. Remove All Digits
# Task: Remove every digit from a string and keep the other characters unchanged.
# Test Case: Input: s = "abc123" → Expected Output: "abc"
# Test Case: Input: s = "Js 101 course" → Expected Output: "Js  course"
# Test Case: Input: s = "2025" → Expected Output: ""

s = input("Enter a string: ")

result = ""

for ch in s:
    if not ("0" <= ch <= "9"):
        result += ch

print(result)


# Q95. Toggle Character Case
# Task: Change lowercase letters to uppercase and uppercase letters to lowercase. Leave digits and spaces unchanged.
# Test Case: Input: s = "HeLLo" → Expected Output: "hEllO"
# Test Case: Input: s = "abcDEF" → Expected Output: "ABCdef"
# Test Case: Input: s = "Js 101" → Expected Output: "jS 101"

s = input("Enter a string: ")

result = ""

for ch in s:
    if "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    elif "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)