# Maximum Number of Non-Overlapping Substrings
# Platform: LeetCode
# Difficulty: Hard
# Topics: Hash Table, String, Greedy, Sorting

"""
This solution first computes the first and last occurrence of each character to build valid substring intervals, expanding each interval dynamically if it encompasses characters with earlier starting points. It then sorts these valid intervals by their end points and uses a greedy approach to select the maximum number of non-overlapping substrings. The time complexity is $O(n + \Sigma^3)$ (where $\Sigma$ is the alphabet size, 26) and the space complexity is $O(n)$ for storing intervals and the result.
"""

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c in first:
            l = first[c]
            r = last[c]
            valid = True
            i = l
            while i <= r:
                char = s[i]
                if first[char] < l:
                    valid = False
                    break
                r = max(r, last[char])
                i += 1
            if valid:
                intervals.append((r, l))

        intervals.sort()

        ans = []
        prev_end = -1
        for r, l in intervals:
            if l > prev_end:
                ans.append(s[l:r+1])
                prev_end = r

        return ans