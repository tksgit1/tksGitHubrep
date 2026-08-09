# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Access them securely using os.environ
database_password = os.environ.get("Test@135mac")
api_key = os.environ.get("128476_mask_secret_tokenmac")

print(f"Successfully loaded database password safely!")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
