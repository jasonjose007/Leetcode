# Merge Strings Alternately
# Difficulty: Easy
# Topics: Two Pointers, String

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1, n2 = len(word1), len(word2)
        limit = min(n1, n2)
        for i in range(limit):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[limit:])
        res.append(word2[limit:])
        return "".join(res)