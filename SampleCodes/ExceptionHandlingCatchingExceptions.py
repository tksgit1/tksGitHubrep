try:
    # This will cause ValueError
    x = int("str")
    inv = 1 / x  # Inverse calculation

except ValueError:
    print("Not Valid!")

except ZeroDivisionError:
    print("Zero has no inverse!")

