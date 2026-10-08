#-----------------------------------------------------------#
#-----------------Q66. Exam Result Analyzer-----------------#
#-----------------------------------------------------------#
mark1 = int(input("Enter subject 1 marks: "))
mark2 = int(input("Enter subject 2 marks: "))
mark3 = int(input("Enter subject 3 marks: "))
attendance = int(input("Enter attendance: "))

total = mark1 + mark2 + mark3
average = total / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")