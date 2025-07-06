/*Знайти середній бал, який ставить певний викладач зі своїх предметів.*/

SELECT AVG(g.grade)
FROM grades g
JOIN subjects s ON g.subject_id = s.id
JOIN teachers t ON s.teacher_id = t.id
WHERE t.full_name = :teacher_name;