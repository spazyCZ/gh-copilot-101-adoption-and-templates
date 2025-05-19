import sys

def main():
    # Skip the script name and convert arguments to integers
    numbers = [int(arg) for arg in sys.argv[1:]]
    total = sum(numbers)
    print(total)

if __name__ == "__main__":
    main()
