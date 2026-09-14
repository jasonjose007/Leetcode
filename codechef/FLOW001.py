# Add Two Numbers
# Platform: CodeChef
# Difficulty: Easy

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    idx = 1
    for _ in range(t):
        if idx + 1 < len(input_data):
            a = int(input_data[idx])
            b = int(input_data[idx+1])
            results.append(str(a + b))
            idx += 2
    print('\n'.join(results))

if __name__ == '__main__':
    solve()