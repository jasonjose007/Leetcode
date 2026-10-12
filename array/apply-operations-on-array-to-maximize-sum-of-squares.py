# Apply Operations on Array to Maximize Sum of Squares
# Platform: LeetCode
# Difficulty: Hard
# Topics: Array, Hash Table, Greedy, Bit Manipulation

"""
This algorithm maximizes the sum of squared elements by greedily distributing the available 1-bits across the $k$ chosen numbers, since squaring heavily favors larger numbers. It first counts the occurrences of each bit position across all numbers in $nums$, reconstructs new numbers by packing these bits from most to least significant, and then sums the squares of the $k$ largest reconstructed numbers modulo $10^9 + 7$. The time complexity is $O(N \log M)$ (where $N$ is the length of $nums$ and $M$ is the maximum value in $nums$), and the space complexity is $O(N)$ to store the processed numbers.
"""

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    bit_counts[b] += 1
        
        final_nums = [0] * len(nums)
        for b in range(30):
            count = bit_counts[b]
            for i in range(count):
                final_nums[i] |= (1 << b)
                
        final_nums.sort(reverse=True)
        
        ans = 0
        for i in range(k):
            ans = (ans + final_nums[i] * final_nums[i]) % MOD
            
        return ans