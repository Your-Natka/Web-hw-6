/*Оцінки студентів у певній групі з певного предмета на останньому занятті.*/

WITH last_date AS (
    SELECT MAX(grade_date) AS date
    FROM grades
    WHERE subject_id = 1
)
SELECT s.full_name, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.group_id = 1 AND g.subject_id = 1 AND g.grade_date = (SELECT date FROM last_date);
