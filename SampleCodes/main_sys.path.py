# main.py
import sys
sys.path.insert(0, "../Dog")  # add Folder_2 path to search list

import module1

print(module1.add(5, 3))      # Output: 8
module1.odd_even(10)          # Output: Even
