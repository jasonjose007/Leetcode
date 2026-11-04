-- Rising Temperature
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- This SQL solution uses an inner self-join to pair each row (`w1`) with the row corresponding to the immediately preceding day (`w2`) using the `DATEDIFF` function. It then filters these paired records using a `WHERE` clause to select the IDs where the current day's temperature (`w1`) is strictly higher than the previous day's (`w2`). Assuming no pre-existing indexes, this approach has a worst-case time complexity of $O(N^2)$ (or $O(N \log N)$ / $O(N)$ if properly indexed) and a space complexity of $O(N)$ to store the intermediate joined results.

SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature