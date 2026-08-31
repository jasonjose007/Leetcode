# Number of Strings That Appear as Substrings in Word
# Difficulty: Easy
# Topics: Array, String

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for p in patterns if p in word)