-- Product Price at a Given Date
-- Platform: LeetCode
-- Difficulty: Medium
-- Topics: Database

-- The query filters records on or before '2019-08-16' and uses the `ROW_NUMBER()` window function (partitioned by `product_id` and ordered by date descending) to find each product's most recent price change. It then performs a `LEFT JOIN` between all unique product IDs and the latest price changes, applying `COALESCE` to default products without prior updates to a price of 10. The time complexity is **$O(N \log N)$** due to the sorting required by the window function (where $N$ is the number of records), and the space complexity is **$O(N)$** to store the intermediate tables.

SELECT
    p.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM Products
) p
LEFT JOIN (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
) lp
    ON p.product_id = lp.product_id AND lp.rn = 1;