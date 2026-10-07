# Q69
text = input()
total = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index = 0
for i in range(len(text)):
    char = text[i]
    total += 1
    if i % 2 == 0:
        even_index += 1
    if char != " ":
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index)
