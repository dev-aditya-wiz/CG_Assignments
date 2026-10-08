#-----------------------------------------------------#
#------------Q30. Scholarship Eligibility-------------#
#-----------------------------------------------------#
marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")