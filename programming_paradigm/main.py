import sys
from robust_division_calculator import safe_divide

def main():
    # Check if exactly 3 arguments are provided: script name, numerator, denominator
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are retrieved as strings from sys.argv
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function
    result = safe_divide(numerator, denominator)
    
    # Print the result or error message returned by safe_divide
    print(result)

if __name__ == "__main__":
    main()