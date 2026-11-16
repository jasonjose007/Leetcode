-- Tree Node
-- Platform: LeetCode
-- Difficulty: Medium
-- Topics: Database

-- Although labeled as a Python solution, this is an SQL query that classifies each row in the `Tree` table using a `CASE` expression. It assigns `'Root'` if a node has no parent (`p_id IS NULL`), `'Inner'` if its `id` appears in the subquery of existing non-null `p_id` values (meaning it has at least one child), and `'Leaf'` otherwise. For $N$ nodes, a modern SQL optimizer typically executes this in $O(N)$ time and $O(N)$ space by hashing or indexing the subquery results, though a naive unoptimized scan would take $O(N^2)$ time.

SELECT 
    id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree