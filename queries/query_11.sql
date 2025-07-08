/*Середній бал, який певний викладач ставить певному студентові.*/

SELECT ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = 1 AND g.student_id = 1;