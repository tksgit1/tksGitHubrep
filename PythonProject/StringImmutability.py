s = "geeksforGeeks"
#s = "G" + s[1:]
s = "G" + s[2:]
print('s -->', s)
print('s[2:] -->', s[2:])

#String Slicing and Reassembling
n1 = "Aarun"
n2 = "T" + n1[1:]
print('n2 = "T" + n1[1:] -->', n2)

#String Concatenation
v1 = "Hello"
# Creates a new string with the concatenated result
v2 = v1 + ", world!"
print('v2 = v1 + ", world!" -->', v2)


l1 = ["Hello", "world!"]

# Joins the list elements with a space separator
l2 = " ".join(l1)
print('l2 = " ".join(l1) -->', l2)



n1 = "Geeks"
# Insert the value of 'name' into the string using format()
n2 = "Hello {} For Geeks".format(n1)
print('Hello {} For Geeks".format(n1) -->', n2)



