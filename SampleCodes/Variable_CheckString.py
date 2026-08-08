print("#Check String")
txt = "The best things in life are free!"
print("free" in txt)

print("\n#Use it in an if statement")
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print("\n#Check if NOT")
txt = "The best things in life are free!"
print("expensive" not in txt)

print("\n#Use it in an if statement")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
