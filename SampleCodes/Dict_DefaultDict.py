
from collections import defaultdict

# Creating a defaultdict with default value of 0 (int)
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]

# Counting occurrences of each element in the list
for i in L:
    d[i] += 1  # No need to check key existence; default is 0

print(d)
