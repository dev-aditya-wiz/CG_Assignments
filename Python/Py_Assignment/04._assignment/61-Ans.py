#----------------------------------------------------#
#-------------Q61. Number Digit Analyzer-------------#
#----------------------------------------------------#
number = int(input("Enter a positive integer: "))

if number < 10:
    print("One Digit")
elif number < 100:
    print("Two Digits")
elif number < 1000:
    print("Three Digits")
else:
    print("Four or More Digits")