# Minimum Insertions to Balance a Parentheses String
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Stack, Greedy, Bracket Sequences

"""
This greedy algorithm uses a single pass to track the count of required closing parentheses (`needed_right`), where each `(` initially expects two `)`. It increments the insertion count (`ans`) whenever a new `(` is encountered while an odd number of `)` is still needed (forcing a `)` insertion), or when an excess `)` appears with no matching `(` (forcing a `(` insertion). 

The algorithm has a **time complexity of $O(n)$**, where $n$ is the length of the string, and an **auxiliary space complexity of $O(1)$**.
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        needed_right = 0
        for char in s:
            if char == '(':
                if needed_right % 2 != 0:
                    ans += 1
                    needed_right -= 1
                needed_right += 2
            else:
                needed_right -= 1
                if needed_right < 0:
                    ans += 1
                    needed_right += 2
        return ans + needed_right