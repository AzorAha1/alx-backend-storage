--- band with glam rock
SELECT band_name, (2022 - formed) as lifespan
from metal_bands
ORDER BY lifespan DESC
