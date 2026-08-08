
t = (1, 2, 3, 4, 5)
# Reverse the tuple by iterating through the indices in reverse order
rev = tuple(t[i] for i in range(len(t) - 1, -1, -1))
print(rev)

