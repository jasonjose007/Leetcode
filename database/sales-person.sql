-- Sales Person
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- Note that the provided snippet is a SQL query rather than a Python solution. It solves the problem using a correlated `NOT EXISTS` subquery (an anti-join) that inspects each row in `SalesPerson` and excludes anyone who has an entry in `Orders` joined to a `Company` row with `name = 'RED'`. Because execution depends on the database engine and indexing, time complexity typically ranges from $O(S + O + C)$ using indexes or hash joins to $O(S \cdot O \cdot C)$ for unindexed nested-loop scans (where $S$, $O$, and $C$ are the row counts of the three tables), while auxiliary space complexity ranges from $O(1)$ for streaming nested loops up to $O(O + C)$ if intermediate hash tables are constructed.

SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    INNER JOIN Company c ON o.com_id = c.com_id
    WHERE o.sales_id = s.sales_id
      AND c.name = 'RED'
);