# First and Last Digit
# Platform: CodeChef
# Difficulty: Easy

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        first = int(s[0])
        last = int(s[-1])
        results.append(str(first + last))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()