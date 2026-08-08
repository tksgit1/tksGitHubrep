from collections import deque

# Initializing deque with initial values
de = deque([1, 2, 3])

# Append 4 to the right end of deque
de.append(4)

# Print deque after appending to the right
print("The deque after appending at right is :")
print(de)

# Append 6 to the left end of deque
de.appendleft(6)

# Print deque after appending to the left
print("The deque after appending at left is :")
print(de)

