# Minimum Number of Changes to Make Binary String Beautiful
# Platform: LeetCode
# Difficulty: Medium
# Topics: String

"""
The algorithm uses a greedy approach based on the property that any "beautiful" binary string can be partitioned into uniform pairs of `"00"` or `"11"`. It iterates through the string with a step size of 2 to inspect each non-overlapping pair of adjacent characters, incrementing a counter whenever the two characters differ (since one change is required to make them match). This solution runs in $O(n)$ time complexity, where $n$ is the length of the string `s`, and uses $O(1)$ space complexity as it only maintains a single counter variable.
"""

class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans