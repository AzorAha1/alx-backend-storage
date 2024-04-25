-- count fans origin
SELECT origin, COUNT(DISTINCT fans) AS nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
