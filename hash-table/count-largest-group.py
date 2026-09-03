# Count Largest Group
# Difficulty: Easy
# Topics: Hash Table, Math, Counting

class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = [0] * 50
        for i in range(1, n + 1):
            s = 0
            temp = i
            while temp > 0:
                s += temp % 10
                temp //= 10
            counts[s] += 1
        
        max_size = max(counts)
        return counts.count(max_size)