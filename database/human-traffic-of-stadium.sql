-- Human Traffic of Stadium
-- Platform: LeetCode
-- Difficulty: Hard
-- Topics: Database

-- *(Note: the provided code is SQL rather than Python.)* It implements the "gaps and islands" algorithm by first filtering for rows where `people >= 100` and subtracting `ROW_NUMBER() OVER (ORDER BY id)` from `id` so that every consecutive run of `id`s shares the same group key (`grp`). Next, it computes the length of each run with `COUNT(*) OVER (PARTITION BY grp)`, filters for sequences with at least 3 rows, and sorts the final output by `visit_date`. For a table of $N$ rows, the time complexity is $O(N \log N)$ due to the sorting required for the window functions and final `ORDER BY`, and the space complexity is $O(N)$ to hold the intermediate CTE rows and sorting buffers.

WITH Filtered AS (
    SELECT
        id,
        visit_date,
        people,
        CAST(id AS SIGNED) - CAST(ROW_NUMBER() OVER (ORDER BY id) AS SIGNED) AS grp
    FROM Stadium
    WHERE people >= 100
),
Grouped AS (
    SELECT
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM Filtered
)
SELECT
    id,
    visit_date,
    people
FROM Grouped
WHERE cnt >= 3
ORDER BY visit_date ASC;