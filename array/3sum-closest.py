from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target, 0, len(nums) - 1)

    def KSumClosest(self, nums: List[int], k: int, target: int, start: int, end: int) -> int:
        length = end - start + 1
        
        if length == k:
            return sum(nums[start:start + k])

        min_sum = sum(nums[start:start + k])
        if min_sum >= target:
            return min_sum

        max_sum = sum(nums[end - k + 1:end + 1])
        if max_sum <= target:
            return max_sum
        
        if k == 2:
            closest_2sum = nums[start] + nums[end]
            l, r = start, end
            while l < r:
                curr_2sum = nums[l] + nums[r]
                if curr_2sum == target:
                    return target
                if abs(curr_2sum - target) < abs(closest_2sum - target):
                    closest_2sum = curr_2sum
                if curr_2sum > target:
                    r -= 1
                else:
                    l += 1
            return closest_2sum

        closest = min_sum
        for i in range(start, end - k + 2):
            if i > start and nums[i] == nums[i - 1]:
                continue
                
            current = self.KSumClosest(nums, k - 1, target - nums[i], i + 1, end) + nums[i]
            
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                closest = current

        return closest