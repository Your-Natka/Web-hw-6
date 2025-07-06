/*Знайти список студентів у певній групі.*/

SELECT s.full_name
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.name = :group_name;