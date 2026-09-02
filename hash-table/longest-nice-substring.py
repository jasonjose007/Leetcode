# Longest Nice Substring
# Difficulty: Easy
# Topics: Hash Table, String, Divide and Conquer, Bit Manipulation, Sliding Window

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        best_start, best_len = -1, -1
        
        for i in range(n):
            seen = set()
            bad_count = 0
            for j in range(i, n):
                c = s[j]
                if c not in seen:
                    seen.add(c)
                    if c.swapcase() in seen:
                        bad_count -= 1
                    else:
                        bad_count += 1
                if bad_count == 0:
                    length = j - i + 1
                    if length > best_len:
                        best_len = length
                        best_start = i
                        
        if best_len == -1:
            return ""
        return s[best_start:best_start + best_len]