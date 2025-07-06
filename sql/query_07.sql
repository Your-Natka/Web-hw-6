/*Знайти оцінки студентів у окремій групі з певного предмета.*/

SELECT st.full_name, g.grade
FROM grades g
JOIN students st ON g.student_id = st.id
JOIN groups gr ON st.group_id = gr.id
JOIN subjects sb ON g.subject_id = sb.id
WHERE gr.name = :group_name AND sb.name = :subject_name;