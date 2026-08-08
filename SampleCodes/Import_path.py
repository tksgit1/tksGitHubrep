'''
# main.py
import sys
sys.path.insert(0, "../Folder_2")  # add Folder_2 path to search list

import module1

print(module1.add(5, 3))      # Output: 8
module1.odd_even(10)          # Output: Even
'''
"""
#option 1
import sys
from pathlib import Path

# Get the directory of the current script, go up one level, and find Folder_2
folder2_path = Path(__file__).resolve().parent.parent / "Folder_2"
sys.path.insert(0, str(folder2_path))

import module1

print(module1.add(5, 3))      # Output: 8
module1.odd_even(10)          # Output: Even
"""
'''
#option 2
import os
import sys

# Build the absolute path dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
folder2_path = os.path.abspath(os.path.join(current_dir, "../Folder_2"))
sys.path.insert(0, folder2_path)

import module1

print(module1.add(5, 3))
module1.odd_even(10)
'''
"""
#1. DC
import sys
from pathlib import Path

# Get script directory
script_dir = Path(__file__).resolve().parent
print(f"--- DIAGNOSTICS ---")
print(f"Script location: {script_dir}")
print(f"Looking for Folder_2 at: {script_dir / 'Folder_2'}")
print(f"Looking for Folder_2 at: {script_dir.parent / 'Folder_2'}")
print(f"-------------------")

# Try importing
import module1
"""
#2. Fix
import sys
from pathlib import Path

# Points to /Users/tankimseah/PycharmProjects/SampleCodes/Folder_2
folder2_path = Path(__file__).resolve().parent / "Folder_2"
sys.path.insert(0, str(folder2_path))

import module1



