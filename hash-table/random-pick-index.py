# Random Pick Index
# Platform: LeetCode
# Difficulty: Medium
# Topics: Hash Table, Math, Reservoir Sampling, Randomized

"""
This solution preprocesses the input array using a hash table (`defaultdict`) to map each unique number to a list of its indices. During the `pick` operation, it directly retrieves the target's index list and uses `random.choice` to uniformly select an index at random. Preprocessing requires $O(N)$ time and $O(N)$ space (where $N$ is the length of `nums`), while each subsequent `pick` call operates in $O(1)$ time and $O(1)$ space.
"""

class Solution:

    def __init__(self, nums: list[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])