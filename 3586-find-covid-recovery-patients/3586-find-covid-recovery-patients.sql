# Write your MySQL query statement below
WITH first_positive AS (
    SELECT patient_id, MIN(test_date) AS first_pos_date
    FROM covid_tests
    WHERE result = "Positive"
    GROUP BY patient_id
)
SELECT t.patient_id, patient_name, age, recovery_time
FROM(
    SELECT c.patient_id, DATEDIFF(MIN(c.test_date), f.first_pos_date) AS recovery_time
    FROM covid_tests c JOIN first_positive f ON c.patient_id = f.patient_id
    WHERE c.result = "Negative" and c.test_date > f.first_pos_date
    GROUP BY c.patient_id, f.first_pos_date) AS t
    LEFT JOIN patients ON t.patient_id = patients.patient_id
ORDER BY recovery_time, patient_name