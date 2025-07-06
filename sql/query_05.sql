/*Знайти які курси читає певний викладач.*/

SELECT s.name 
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
WHERE t.full_name = :teacher_name;