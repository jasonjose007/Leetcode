# Teemo Attacking
# Difficulty: Easy
# Topics: Array, Simulation

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0
        
        total_duration = 0
        for i in range(len(timeSeries) - 1):
            total_duration += min(duration, timeSeries[i+1] - timeSeries[i])
            
        total_duration += duration
        return total_duration