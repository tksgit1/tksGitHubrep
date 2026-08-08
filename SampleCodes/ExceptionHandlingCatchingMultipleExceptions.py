a = ["10", "twenty", 30]
try:
    # 'twenty' cannot be converted to int
    total = int(a[0]) + int(a[1])

except (ValueError, TypeError) as e:
    print("Error", e)

except IndexError:
    print("Index out of range.")

