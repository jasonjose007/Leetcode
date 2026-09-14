# Find Remainder
# Platform: CodeChef
# Difficulty: Easy

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    results = []
    idx = 1
    for _ in range(T):
        A = int(input_data[idx])
        B = int(input_data[idx+1])
        results.append(str(A % B))
        idx += 2
    print('\n'.join(results))

if __name__ == '__main__':
    solve()