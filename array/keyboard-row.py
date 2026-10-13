# Keyboard Row
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Hash Table, String

"""
The algorithm represents each keyboard row as a character set and checks whether the set of lowercase letters in each word is a subset (`<=`) of any single row. Words whose characters all belong to the same row are collected into a result list and returned. It operates in **$O(N \times L)$ time**, where $N$ is the number of words and $L$ is the average word length, with **$O(1)$ auxiliary space** (excluding the output) since the sets are bounded by the 26 English letters.
"""

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        
        ans = []
        for word in words:
            w_set = set(word.lower())
            if w_set <= r1 or w_set <= r2 or w_set <= r3:
                ans.append(word)
                
        return ans