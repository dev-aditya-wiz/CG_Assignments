#----------------------------#
#-------Date Analyzer--------#
#----------------------------#
date = input()
parts = date.split("-")
day = parts[0]
month = parts[1]
year = parts[2]
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(date[-4:])