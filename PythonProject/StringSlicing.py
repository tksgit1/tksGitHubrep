#substring = s[start : end : step]
s='function with parameters'
print('s[1:4] -->', s[1:4])
#To reverse a string, from the end of the string to the beginning
print('s[::-1] -->', s[::-1])
#Starting index (inclusive), Stopping index (exclusive)
print('s[0:5] -->', s[0:5])
#starting from the 4th character from the end
print('s[-4:] -->', s[-4:])
'''slices the string from the beginning up to the 
3rd character from the end, excluding it'''
print('s[:-3] -->', s[:-3])
'''slices the string from the 5th character from the 
end to the 2nd character from the end, 
excluding the last character.'''
print('s[-5:-2] -->', s[-5:-2])
'''slices the string from the 8th character from the 
end to the 2nd character from the end, 
with a step of 2, taking every second character.'''
print('s[-8:-1:2] -->', s[-8:-1:2])

