# Calculate Digit Sum of a String
# Platform: LeetCode
# Difficulty: Easy
# Topics: String, Simulation

"""
The algorithm repeatedly partitions `s` into consecutive substrings of length at most `k`, converts each substring's characters to integers to compute their digit sum, and joins the resulting sum strings to form the new `s` until `len(s) <= k`. Because the length of `s` shrinks geometrically across iterations (for $k \ge 2$), the total work across all rounds forms a geometric series, giving a time complexity of $O(n)$ where $n$ is the initial length of `s`. The space complexity is $O(n)$ to store the substring slices, the list of sum strings `nxt`, and the newly joined string in each iteration.
"""

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nxt = []
            for i in range(0, len(s), k):
                nxt.append(str(sum(int(c) for c in s[i:i + k])))
            s = "".join(nxt)
        return s