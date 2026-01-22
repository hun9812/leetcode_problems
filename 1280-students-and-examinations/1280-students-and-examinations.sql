# Write your MySQL query statement below
SELECT Stu.student_id, Stu.student_name, Sub.subject_name,
       IFNULL(COUNT(E.subject_name), 0) AS attended_exams
FROM Students AS Stu
     CROSS JOIN Subjects AS Sub
     LEFT OUTER JOIN Examinations AS E 
     ON Stu.student_id = E.student_id and Sub.subject_name = E.subject_name
GROUP BY Stu.student_id, Sub.subject_name
ORDER BY Stu.student_id, Sub.subject_name