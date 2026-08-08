
from collections import deque
t = (1, 2, 3, 4, 5)
deq = deque(t)

# Reverse the deque in place
deq.reverse()

# Convert the reversed deque back to a tuple
rev = tuple(deq)

print(rev)

