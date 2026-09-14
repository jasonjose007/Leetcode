# ATM
# Platform: CodeChef
# Difficulty: Easy

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    X = int(input_data[0])
    Y = float(input_data[1])
    
    if X % 5 == 0 and Y >= X + 0.50:
        ans = Y - X - 0.50
    else:
        ans = Y
        
    print(f"{ans:.2f}")

if __name__ == '__main__':
    solve()