
#Creating a String
print('#Creating a String')
s1 = "GeeksforGeeks"
s2 = " Hi Geek! "

print('s1 -->', s1)
print('s2 -->', s2)

print('')
#length of the String
print('#length of the String')
print('len(s1) -->', len(s1))

print('')
#Multi-line Strings
print('#Multi-line Strings')
s = """I am Learning
Python String on GeeksforGeeks"""
print('s -->', s)

s = '''I'm a 
Geek'''
print('s -->', s)

print('')
#Accessing Characters in String
print('#Accessing Characters in String')
s = "ABCDEF"
print('s[0] -->', s[0])
print('s[4] -->', s[4])

s = "ABCDEF"
print('s[-3] -->', s[-3])
print('s[-5] -->', s[-5])

print('')
#String Slicing
print('#String Slicing')
s = "ABCDEF"
print('s[1:4] -->', s[1:4])
print('s[:3] -->', s[:3])
print('s[3:] -->', s[3:])
print('s[::-1] -->', s[::-1])

print('')
#Looping Through Strings
print('#Looping Through Strings')
s = "ABCDEF"
for char in s:
    print('for char in s -->', char)

print('')
#String Immutability
print('#String Immutability')
s = "aBCDEF"
s = "A" + s[1:]
print('s -->', s)

print('')
#Deleting a String
print('#Deleting a String')
s = "ABC"
del s
#print(' del s -->', s)

print('')
#Updating a String
print('#Updating a String')
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")

print('s1 -->', s1)
print('s2 -->', s2)

print('')
#Common String Methods
print('#Common String Methods')
s = "GeeksforGeeks"
print('len(s) -->', len(s))

print('')
#upper() and lower():
print('#upper() and lower():')
s = "Hello World"
print('s.upper() -->', s.upper())
print('s.lower() -->', s.lower())

print('')
#strip() and replace():
print('#strip() and replace():')
s = "   ABC   "
print('s.strip() -->', s.strip())

s = "Python is fun"
s = s.replace("fun", "awesome")
print('s -->', s)

print('')
#Concatenation:
print('#Concatenation:')
s1 = "Hello"
s2 = "World"
print('s1 + " " + s2 -->', s1 + " " + s2)

print('')
#Repetition:
print('#Repetition:')
s = "Hello "
print('s * 3 -->', s * 3)

print('')
#Using f-strings:
print('#Using f-strings:')
name = "Jake"
age = 22
print('f"Name: {name}, Age: {age}" -->', f"Name: {name}, Age: {age}")

print('')
#Using format():
print('#Using format():')
s = "My name is {} and I am {} years old.".format( "Emily", 22)
print('s -->', s)

print('')
#String Membership Testing
print('#String Membership Testing')
s = "GeeksforGeeks"
print('"Geeks" in s -->', "Geeks" in s)
print('"GfG" in s -->', "GfG" in s)












