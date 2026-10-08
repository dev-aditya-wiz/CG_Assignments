#----------------------------#
#----Student ID Analyzer-----#
#----------------------------#
student_id = input()
parts = student_id.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = parts[3]
last_three = student_id[-3:]
print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll Number: {int(roll_number)}")