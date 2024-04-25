--- band with glam rock
SELECT band_name, COALESCE(split, 2922) - formed as lifespan FROM metal_bands
WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC
