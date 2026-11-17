-- Product Sales Analysis I
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- First, note that the provided code is a SQL query rather than Python; it solves the problem by performing an `INNER JOIN` between the `Sales` and `Product` tables on `product_id` to retrieve each sale's `product_name`, `year`, and `price`. A SQL engine typically executes this equi-join using a hash join—building a hash table on the smaller table (`Product`) and probing it with rows from `Sales`—though the query optimizer may choose a sort-merge or nested-loop join depending on available indexes and table sizes. Assuming a hash join over $N$ rows in `Sales` and $M$ rows in `Product`, the average time complexity is $O(N + M)$ and the auxiliary space complexity is $O(\min(N, M))$ to store the hash table.

SELECT p.product_name, s.year, s.price
FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id;