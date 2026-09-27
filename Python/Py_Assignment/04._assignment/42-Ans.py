#----------------------------------------------------#
#------------Q42. Hostel Room Allocation-------------#
#----------------------------------------------------#
year = int(input("Enter year: "))
attendance = int(input("Enter attendance: "))

if year == 2 or year == 3 or year == 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")