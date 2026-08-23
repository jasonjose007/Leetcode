# Sum Game
# Difficulty: Medium
# Topics: Math, String, Greedy, Game Theory

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        left = num[:mid]
        right = num[mid:]
        
        sl = sum(int(c) for c in left if c != '?')
        ql = left.count('?')
        sr = sum(int(c) for c in right if c != '?')
        qr = right.count('?')
        
        return 2 * (sl - sr) != 9 * (qr - ql)