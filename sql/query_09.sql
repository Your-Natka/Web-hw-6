/*Знайти список курсів, які відвідує студент.*/

SELECT DISTINCT sb.name AS subject_name
FROM grades g
JOIN students st ON g.student_id = st.id
JOIN subjects sb ON g.subject_id = sb.id
WHERE st.full_name = :student_name;
