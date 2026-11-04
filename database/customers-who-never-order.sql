-- Customers Who Never Order
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- This SQL solution uses a `LEFT JOIN` between the `Customers
-- ` and `Orders` tables to pair every customer with their corresponding orders, keeping all customers even if they have no matches. It then filters the results using `WHERE o.customerId IS NULL` to retain only those customers who do not appear in the `Orders` table. Assuming proper indexing, the time complexity is $O(N + M)$ and the space complexity is $O(N + M)$, where $N$ and $M$ are the number of rows in the Customers and Orders tables, respectively.

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL