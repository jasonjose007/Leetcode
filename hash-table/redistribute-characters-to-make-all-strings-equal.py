# Redistribute Characters to Make All Strings Equal
# Platform: LeetCode
# Difficulty: Easy
# Topics: Hash Table, String, Counting

"""
This algorithm counts the total frequency of each character across all words and verifies if every character's count is evenly divisible by the total number of words ($N$). If any character count cannot be distributed equally among the words, the function returns `False`; otherwise, it returns `True`. The time complexity is $O(S)$, where $S$ is the total number of characters across all words, and the space complexity is $O(1)$ because the hash map stores at most 26 unique lowercase English letters.
"""

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        n = len(words)
        counts = Counter()
        for word in words:
            counts.update(word)
        for count in counts.values():
            if count % n != 0:
                return False
        return True