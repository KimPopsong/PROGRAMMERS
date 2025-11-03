SELECT
    e1.id,
    COUNT(e2.id) AS CHILD_COUNT
FROM ecoli_data e1
LEFT JOIN ecoli_data e2
    ON e1.id = e2.parent_id
GROUP BY e1.id
ORDER BY e1.id;
