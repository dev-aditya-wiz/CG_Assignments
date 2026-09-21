#----------------------------#
#-----Character Analyzer-----#
#----------------------------#
character = input()
code = ord(character)
previous = chr(code - 1)
next_character = chr(code + 1)
print(f"Character: {character}")
print(f"Code: {code}")
print(f"Previous: {previous}")
print(f"Next: {next_character}")