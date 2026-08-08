import zipapp
import os

# Create a simple script directory
os.makedirs('myapp1', exist_ok=True)
with open('myapp1/__main__.py', 'w') as f:
  f.write("print('Hello from zipapp!')")

# Create executable zipapp
zipapp.create_archive('myapp1', 'myapp1.pyz')
print('Created myapp1.pyz')

