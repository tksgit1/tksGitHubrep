class Check:
    def __init__(self):
        print("Address of self:", id(self))

obj = Check()
print("Address of object:", id(obj))