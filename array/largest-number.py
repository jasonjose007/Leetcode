# Largest Number
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, String, Greedy, Sorting

"""
The algorithm uses a greedy approach by converting the numbers to strings and sorting them in descending order using a custom comparator that determines whether $a+b$ or $b+a$ produces a larger value. Once sorted, the strings are joined together to form the largest possible number, with an edge-case check returning `"0"` if the leading value is zero. The time complexity is $O(N \log N \cdot K)$ due to the string-comparison-based sorting, and the space complexity is $O(N \cdot K)$ to store the string representations, where $N$ is the number of elements and $K$ is the maximum number of digits in an element.
"""

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = [str(x) for x in nums]
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
                
        strs.sort(key=functools.cmp_to_key(compare))
        
        result = "".join(strs)
        if result[0] == "0":
            return "0"
            
        return result