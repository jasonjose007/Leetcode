# Ransom Note
# Difficulty: Easy
# Topics: Hash Table, String, Counting

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        return not (Counter(ransomNote) - Counter(magazine))