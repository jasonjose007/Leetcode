# Reverse The Number
# Platform: CodeChef
# Difficulty: Easy

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        n_str = input_data[i]
        reversed_n = int(n_str[::-1])
        results.append(str(reversed_n))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()