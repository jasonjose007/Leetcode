-- Rising Temperature
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- This SQL solution uses a self-join on the `Weather` table to pair each record (`w1`) with the record corresponding to the immediately preceding day (`w2`) using the `DATEDIFF` function. It then filters these matched pairs to select the IDs where the current day's temperature is strictly higher than the previous day's. The time complexity is $O(N^2)$ for an unindexed nested-loop join (reducible to $O(N)$ with proper indexing on `recordDate`), and the space complexity is $O(N)$ to store the intermediate join results, where $N$ is the total number of rows.

SELECT w1.id
FROM Weather w1
JOIN Weather w2 
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature