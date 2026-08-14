# Maximum Length Substring With Two Occurrences
# Difficulty: Easy
# Topics: Hash Table, String, Sliding Window

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_counts = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            char_counts[char] = char_counts.get(char, 0) + 1
            while char_counts[char] > 2:
                char_counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len