#----------------------------#
#---------Input Code---------#
#----------------------------#
sentence = input()
words = sentence.split()
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Total words: {len(words)}")