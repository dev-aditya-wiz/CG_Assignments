students = 23
students_per_group = 5

complete_groups = students // students_per_group
remaining_students = students % students_per_group

print("Complete groups:", complete_groups)
print("Remaining students:", remaining_students)