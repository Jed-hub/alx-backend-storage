-- ranks country origins of bands ordered by the number of fans
SELECT band_name,
(COUNT(split) - COUNT(formed)) AS lifespan
FROM metal_bands
WHERE style='Glam rock'
GROUP BY band_name
ORDER BY (COUNT(split) - COUNT(formed)) DESC;
