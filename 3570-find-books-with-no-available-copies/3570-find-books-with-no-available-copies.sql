# Write your MySQL query statement below
SELECT l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies as current_borrowers
FROM library_books AS l JOIN
    (SELECT book_id, count(*) as borrow_count
    FROM borrowing_records
    WHERE return_date is NULL
    GROUP BY book_id) AS b
    ON l.book_id = b.book_id
WHERE l.total_copies = b.borrow_count
ORDER BY l.total_copies DESC, l.title ASC