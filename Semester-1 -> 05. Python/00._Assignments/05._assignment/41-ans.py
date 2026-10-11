# # Q41
# text = input()
# target = input()
# position = -1
# index = 0
# for char in text:
#     if char == target and position == -1:
#         position = index
#     index += 1
# if position == -1:
#     print("Not Found")
# else:
#     print(position)



word = input("Enter a string : ")
target = input("Enter a character to find : ")
found = False
for char in word:
    if char == target:
        found = True