# Write your MySQL query statement below
WITH rating_filter AS(
    SELECT book_id, SUM(IF(session_rating > 3, 1, 0)) AS sum_high, SUM(IF(session_rating < 3, 1, 0))
           AS sum_low, MAX(session_rating)-MIN(session_rating) AS rating_spread, COUNT(*) AS entire
    FROM reading_sessions
    WHERE book_id in (SELECT book_id FROM reading_sessions GROUP BY book_id HAVING COUNT(*)>=5)
    GROUP BY book_id
)

SELECT r.book_id, b.title, b.author, b.genre, b.pages, r.rating_spread,
       ROUND((sum_high+sum_low) / entire ,2) AS polarization_score 
FROM rating_filter r JOIN books b
     ON r.book_id = b.book_id
WHERE r.sum_high != 0 and r.sum_low != 0
HAVING polarization_score >= 0.6
ORDER BY polarization_score DESC, title DESC