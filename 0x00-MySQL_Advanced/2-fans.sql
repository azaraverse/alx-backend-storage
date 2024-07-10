-- A script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- first select the columns to use from the specified table and group them by origin and in descending order by total fans
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
