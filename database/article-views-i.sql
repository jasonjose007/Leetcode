-- Article Views I
-- Platform: LeetCode
-- Difficulty: Easy
-- Topics: Database

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;