-- Script que lista bandas de Glam rock ordenadas por longevidad hasta 2022
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;

