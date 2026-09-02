# Maximum Number of Words You Can Type
# Difficulty: Easy
# Topics: Hash Table, String

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split()
        ans = 0
        for word in words:
            if not any(char in broken_set for char in word):
                ans += 1
        return ans