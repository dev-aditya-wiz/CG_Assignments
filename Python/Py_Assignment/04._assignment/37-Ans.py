#---------------------------------------------------------#
#------------Q37. Driving License Eligibility-------------#
#---------------------------------------------------------#
age = int(input("Enter age: "))
test_status = input("Enter test status: ")

if age >= 18:
    if test_status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")