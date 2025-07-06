/*Знайти середній бал у групах з певного предмета.*/

SELECT gr.name AS group_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.name = :subject_name
GROUP BY gr.id
ORDER BY avg_grade DESC;
