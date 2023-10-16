-- ranked by their longevity

SELECT band_name, TIMESTAMPDIFF(YEAR, formed, split) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
