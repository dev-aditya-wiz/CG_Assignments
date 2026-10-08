#-------------------------------------#
#--------Student Code Formatter-------#
#-------------------------------------#
student_code = input()
parts = student_code.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]
code = degree + "/" + branch + "/" + roll
print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {code}")