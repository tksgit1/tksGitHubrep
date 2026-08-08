
from collections import deque

# Initialize deque with initial values
de = deque([6, 1, 2, 3, 4])

# Delete element from the right end (removes 4)
de.pop()

# Print deque after deletion from the right
print("The deque after deleting from right is :")
print(de)

# Delete element from the left end (removes 6)
de.popleft()

# Print deque after deletion from the left
print("The deque after deleting from left is :")
print(de)

