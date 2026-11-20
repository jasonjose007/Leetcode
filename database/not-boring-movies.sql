-- Not Boring Movies
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- This query filters the `Cinema` table to extract records with an odd `id` (`MOD(id, 2) = 1`) and a `description` that is not "boring", then sorts the matching rows by `rating` in descending order. 
-- 
-- The overall time complexity is **$O(N \log N)$** due to the sorting step (where $N$ is the number of rows in the table), while the initial filtering takes linear time. The space complexity is **$O(N)$** to store and sort the filtered result set.

SELECT id, movie, description, rating
FROM Cinema
WHERE MOD(id, 2) = 1
  AND description <> 'boring'
ORDER BY rating DESC;