class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < min_prefix_sum:
                min_prefix_sum = current_sum
        return max(1, 1 - min_prefix_sum)