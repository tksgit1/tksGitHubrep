
#!/usr/bin/env python
import argparse
from math_operations_kseahtan.calculate import run_calculator

def main():
    parser = argparse.ArgumentParser(description="Run math operations.")
    parser.add_argument("num1", type=float, nargs="?", default=None, help="The first number")
    parser.add_argument("num2", type=float, nargs="?", default=None, help="The second number")
    parser.add_argument("operation", type=str, nargs="?", default=None, help="The operation to perform")

    args = parser.parse_args()
    run_calculator(args.num1, args.num2, args.operation)

if __name__ == "__main__":
    main()
