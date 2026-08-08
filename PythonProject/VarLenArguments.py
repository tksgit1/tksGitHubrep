print('def print_names(*names):')
print('for name in names:')
print('print(name)')

def print_names(*names):
    for name in names:
        print(name)

print('')
print('print_names("Alice", "Bob", "Charlie") -->', end='')
print_names("Alice" +', '+ "Bob" +', '+ "Charlie")
# Output: Alice, Bob, Charlie

