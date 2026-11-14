-- Project Employees I
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

-- First, note that the provided snippet is a **SQL** query rather than Python code; it solves the problem by inner-joining the `Project` and `Employee` tables on `employee_id`. It then groups the combined rows by `project_id` and computes the average `experience_years` per project, rounded to two decimal places. Depending on the database query planner, using a hash join and hash aggregation gives an average-case time and space complexity of $O(P + E)$—where $P$ and $E$ are the row counts of `Project` and `Employee`—while sort-based execution takes $O(P \log P + E \log E)$ time.

SELECT 
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM 
    Project p
JOIN 
    Employee e ON p.employee_id = e.employee_id
GROUP BY 
    p.project_id