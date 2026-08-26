# Shortest and Lexicographically Smallest Beautiful String
# Difficulty: Medium
# Topics: String, Sliding Window

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, char in enumerate(s) if char == '1']
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        best_sub = ""
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start:end + 1]
            length = len(sub)
            
            if length < min_len:
                min_len = length
                best_sub = sub
            elif length == min_len:
                if sub < best_sub:
                    best_sub = sub
                    
        return best_sub