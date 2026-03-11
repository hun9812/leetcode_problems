# Write your MySQL query statement below
# 5개 이상의 다른 콘텐츠 아이템
# 60%이상이 같은 리엑션

WITH user_react_count AS(
    SELECT user_id, reaction, COUNT(reaction) AS each_count
    FROM reactions
    GROUP BY user_id, reaction
)

SELECT u.user_id, u.reaction AS dominant_reaction, ROUND(each_count/total_count, 2) AS reaction_ratio
FROM user_react_count u LEFT JOIN 
     (SELECT user_id, COUNT(*) AS total_count FROM reactions GROUP BY user_id) AS t
     ON u.user_id = t.user_id
WHERE
    total_count >= 5 and
    (each_count/total_count) > 0.6
ORDER BY reaction_ratio DESC, user_id ASC
