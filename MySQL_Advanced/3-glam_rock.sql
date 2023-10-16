-- ranked by their longevity
SELECT band_name, IFNULL(TIMESTAMPDIFF(YEAR, MIN(formed), MAX(split)), 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
GROUP BY band_name
ORDER BY lifespan DESC;
