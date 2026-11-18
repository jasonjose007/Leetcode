-- Friend Requests II: Who Has the Most Friends
-- Platform: LeetCode
-- Difficulty: Medium
-- Topics: Database

-- This snippet is actually SQL rather than Python; it combines `requester_id` and `accepter_id` into a single column with `UNION ALL` so each accepted request counts toward both users, then groups by `id` to tally each user's total friends. It applies the `RANK()` window function ordered by friend count descending and filters for `rnk = 1`, which returns the user(s) with the most friends while preserving ties. For $N$ rows in `RequestAccepted` and $U$ unique users ($U \le 2N$), the query runs in $O(N + U \log U)$ time (worst-case $O(N \log N)$) due to aggregation and sorting, and uses $O(N)$ space to hold the $2N$ combined IDs and intermediate grouping/ranking state.

WITH RankedFriends AS (
    SELECT
        id,
        COUNT(*) AS num,
        RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM (
        SELECT requester_id AS id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS id FROM RequestAccepted
    ) AS all_friends
    GROUP BY id
)
SELECT id, num
FROM RankedFriends
WHERE rnk = 1;