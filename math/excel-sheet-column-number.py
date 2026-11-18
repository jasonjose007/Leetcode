# Excel Sheet Column Number
# Platform: LeetCode
# Difficulty: Easy
# Topics: Math, String

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for ch in columnTitle:
            res = res * 26 + (ord(ch) - 64)
        return res