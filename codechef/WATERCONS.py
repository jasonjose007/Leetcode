# Water Consumption
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
        x = int(input_data[i])
        if x >= 2000:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()