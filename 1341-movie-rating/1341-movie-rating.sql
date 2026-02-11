# Write your MySQL query statement below
WITH most_watch AS (
    SELECT U.name AS results
    FROM MovieRating M JOIN Users U
    ON U.user_id = M.user_id
    GROUP BY M.user_id
    ORDER BY COUNT(*) DESC, U.name
    LIMIT 1
)

(SELECT results
FROM most_watch)
UNION ALL
(SELECT M.title AS results
FROM MovieRating MR JOIN Movies M
ON MR.movie_id = M.movie_id
WHERE MR.created_at >= "2020-02-01" and MR.created_at < "2020-03-01"
GROUP BY MR.movie_id
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1
)