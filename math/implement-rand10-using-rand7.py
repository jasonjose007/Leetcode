# Implement Rand10() Using Rand7()
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, Rejection Sampling, Randomized, Probability and Statistics

"""
This solution uses the **rejection sampling** algorithm by generating a uniformly distributed random integer from 1 to 49 using a 7x7 grid formed by two independent calls to `rand7()`. It then discards any value greater than 40 to ensure the remaining 40 values map evenly into 10 distinct outcomes using modulo arithmetic. The expected **time complexity** is $O(1)$ (though technically unbounded in the worst case, the expected number of loops is small at $49/40$), and the **space complexity** is $O(1)$ as it uses a constant amount of memory.
"""

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return 1 + (idx - 1) % 10