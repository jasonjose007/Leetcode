# Count Commas in Range II
# Difficulty: Medium
# Topics: Math

class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        k = 1
        while True:
            limit = 10 ** (3 * k)
            if limit > n:
                break
            ans += n - limit + 1
            k += 1
        return ans