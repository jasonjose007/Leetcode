# Oneful Pairs
# Platform: CodeChef
# Difficulty: Easy
# Topics: Python

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    if a + b + a * b == 111:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()