SELECT
    animal_id,
    name,
    DATE_FORMAT(datetime, '%Y-%m-%d') AS '날짜'
FROM
    animal_ins
ORDER BY
    animal_id ASC;
