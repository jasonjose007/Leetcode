# Number of Students Doing Homework at a Given Time
# Difficulty: Easy
# Topics: Array

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(1 for s, e in zip(startTime, endTime) if s <= queryTime <= e)