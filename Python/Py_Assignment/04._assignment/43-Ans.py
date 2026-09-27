#---------------------------------------------------#
#------------Q43. Internet Plan Upgrade-------------#
#---------------------------------------------------#
plan = input("Enter current plan: ")
usage = int(input("Enter monthly usage: "))

if plan == "basic":
    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")