# Write your MySQL query statement below
WITH for_valid AS(
    SELECT
        ip,
        SUBSTRING_INDEX(ip, ".", 1) AS first,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, ".", 2), ".", -1) AS second,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, ".", 3), ".", -1) AS third,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, ".", 4), ".", -1) AS forth,
        LENGTH(ip) - CHAR_LENGTH(REPLACE(ip, ".", "")) AS dot_count
    FROM logs
)

SELECT
    ip, COUNT(*) AS invalid_count
FROM
    for_valid
WHERE
    (dot_count != 3) or
    (first > 255) or (second > 255) or (third > 255) or (forth > 255) or
    (LENGTH(first) != 1 and LEFT(first, 1) = "0") or
    (LENGTH(second) != 1 and LEFT(second, 1) = "0") or
    (LENGTH(third) != 1 and LEFT(third, 1) = "0") or
    (LENGTH(forth) != 1 and LEFT(forth, 1) = "0")
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC