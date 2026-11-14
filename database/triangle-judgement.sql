-- Triangle Judgement
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- Note that the provided code is actually an SQL query rather than a Python solution. For each row in the `Triangle` table, the algorithm applies the triangle inequality theorem by checking if the sum of every pair of side lengths is strictly greater than the remaining side, returning `'Yes'` if all three conditions hold and `'No'` otherwise. Because it performs constant-time arithmetic and logical checks once per row across $N$ rows, the time complexity is $O(N)$, while the space complexity is $O(1)$ auxiliary space (or $O(N)$ if counting the output result set).

SELECT x, y, z, IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle
FROM Triangle;