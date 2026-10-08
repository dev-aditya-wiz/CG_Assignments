#----------------------------#
#---------Input Code---------#
#----------------------------#
text = "ABCDEFGHIJ"
print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])

#----------------------------#
#---------Output Code--------#
#----------------------------#
# Input: text[2:8:2]
# Output: CEG
#- Start: 2
#- Stop: 8
#- Step: 2

# Input: text[8:2:-2]
# Output: IGE
#- Start: 8
#- Stop: 2
#- Step: -2

# Input: text[::-2]
# Output: JHFDB
#- Start: None
#- Stop: None
#- Step: -2