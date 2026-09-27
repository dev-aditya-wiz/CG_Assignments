#------------------------------------------------#
#---------------Q24. BMI Category----------------#
#------------------------------------------------#
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")