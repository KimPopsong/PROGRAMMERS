SELECT 
    COUNT(*) AS FISH_COUNT
FROM
    fish_info
WHERE
    length IS NULL;
