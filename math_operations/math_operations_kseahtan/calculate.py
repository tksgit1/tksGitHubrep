
HISTORY_FILE = "history.txt"
import sys
import os
from datetime import datetime

from math_operations_kseahtan.basic.add import add
from math_operations_kseahtan.basic.subtract import subtract
from math_operations_kseahtan.advanced.multiply import multiply
from math_operations_kseahtan.advanced.divide import divide
from math_operations_kseahtan.advanced.exponent import exponent
from math_operations_kseahtan.advanced.square_root import square_root


def log_history(entry):
    """Appends a single calculation entry with a timestamp to history.txt."""
    # This generates the text string for the current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CRITICAL: Make sure {timestamp} is inside the brackets, not 0
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {entry}\n")

def display_history():
    """Reads and displays the calculation history file."""
    print("\n" + "-" * 30)
    print("      CALCULATION HISTORY")
    print("-" * 30)
    if not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0:
        print("No calculation history found.")
    else:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    print("-" * 30)

def clear_history():
    """Wipes all logged entries inside history.txt."""
    confirm = input("⚠️ Are you sure you want to clear all history? (y/n): ").strip().lower()
    if confirm == 'y':
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            file.write("")  # Overwrites file with empty text
        print("🗑️ Calculation history has been cleared successfully.")
    else:
        print("Operation cancelled.")


def print_menu():
    print("\n" + "="*30)
    print("      MATH OPERATIONS")
    print("="*30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent (Base^Power)")
    print("6. Square Root")
    print("7. View Calculation History")
    print("8. Clear Calculation History")
    print("9. Exit")
    print("="*30)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def start_calculator():
    print("Performing calculation setup...")
    while True:
        print_menu()
        choice = input("Select an option (1-8): ").strip()


    # Change exit selection index matching from 8 to 9
        if choice == '9':
            print("\nGoodbye!")
            sys.exit()

        if choice == '7':
            display_history()
            continue

        if choice == '8':
            clear_history()
            continue

        # Keep valid operation checks restricted to 1 through 6
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("❌ Invalid choice. Please pick a number between 1 and 9.")
            continue

        if choice == '6':
            num1 = get_number("Enter the number: ")
            num2 = None
        else:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number (or power): ")

        try:
            result_str = ""
            if choice == '1':
                res = add(num1, num2)
                result_str = f"{num1} + {num2} = {res}"
            elif choice == '2':
                res = subtract(num1, num2)
                result_str = f"{num1} - {num2} = {res}"
            elif choice == '3':
                res = multiply(num1, num2)
                result_str = f"{num1} * {num2} = {res}"
            elif choice == '4':
                res = divide(num1, num2)
                result_str = f"{num1} / {num2} = {res}"
            elif choice == '5':
                res = exponent(num1, num2)
                result_str = f"{num1} ^ {num2} = {res}"
            elif choice == '6':
                res = square_root(num1)
                result_str = f"√{num1} = {res}"

            print(f"✅ Result: {result_str}")
            log_history(result_str)

        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero.")
        except ValueError as e:
            print(f"❌ Error: {e}")


def execute_operation(num1, num2, operation):
    if operation == "add":
        print(f"\nResult: {add(num1, num2)}")
    # Remove any nested "def log_history", "def print_menu", etc. from here!

def run_calculator(num1=None, num2=None, operation=None):
    if num1 is not None and num2 is not None and operation is not None:
        execute_operation(num1, num2, operation)
    else:
        # Launch your menu mode here
        start_calculator()


# !/usr/bin/env python
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run math operations.")

    # Adding nargs="?" makes these arguments completely optional
    # If you don't provide them, they default to None
    parser.add_argument("num1", type=float, nargs="?", default=None, help="The first number")
    parser.add_argument("num2", type=float, nargs="?", default=None, help="The second number")
    parser.add_argument("operation", type=str, nargs="?", default=None, help="The operation to perform")

    args = parser.parse_args()

    # This will now pass None values to your function when run without arguments
    run_calculator(args.num1, args.num2, args.operation)
