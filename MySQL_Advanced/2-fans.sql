-- Script que clasifica los origenes de las bandas ordenados por cantidad de fans
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;

