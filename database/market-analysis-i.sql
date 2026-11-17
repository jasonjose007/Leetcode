-- Market Analysis I
-- Platform: LeetCode
-- Difficulty: Medium
-- Topics: Database

-- Note that the provided code is actually a SQL query rather than Python; it uses a `LEFT JOIN` from `Users` to `Orders` with the 2019 date filter placed inside the `ON` clause so that users without any 2019 orders are still retained with `NULL` order values. It then groups the result by `user_id` and `join_date` and applies `COUNT(o.order_id)`, which ignores `NULL`s to output `0` for users with no qualifying purchases. Assuming a typical hash join and hash aggregation (depending on the database engine and available indexes), the query runs in $O(U + O)$ time and $O(U + O)$ space, where $U$ is the number of users and $O$ is the number of orders.

SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
    AND o.order_date >= '2019-01-01'
    AND o.order_date < '2020-01-01'
GROUP BY
    u.user_id,
    u.join_date;