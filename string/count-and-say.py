# Count and Say
# Platform: LeetCode
# Difficulty: Medium
# Topics: String

"""
This algorithm uses an iterative simulation with a two-pointer run-length encoding (RLE) technique, counting contiguous identical digits in the current string and appending the format `[count][digit]` to construct the next term. 

Both the time complexity and space complexity are **$O(M)$** (roughly **$O(1.3^n)$**), where $M$ is the length of the $n$-th sequence, because each character is scanned linearly per step and the string length grows exponentially at a rate determined by Conway's constant ($\lambda \approx 1.3035$).
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            next_s = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                next_s.append(str(j - i))
                next_s.append(s[i])
                i = j
            s = "".join(next_s)
        return s