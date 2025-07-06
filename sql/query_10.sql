/*Список курсів, які певному студенту читає певний викладач.*/

SELECT DISTINCT sb.name
FROM grades g
JOIN students st ON g.student_id = st.id
JOIN subjects sb ON g.subject_id = sb.id
JOIN teachers t ON sb.teacher_id = t.id
WHERE st.full_name = :student_name AND t.full_name = :teacher_name;