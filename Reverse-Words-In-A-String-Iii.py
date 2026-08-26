# Reverse Words in a String III
# Difficulty: Easy
# Topics: Two Pointers, String

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))