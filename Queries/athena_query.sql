SELECT producto, SUM(total) as ventas
FROM ventas_procesado
WHERE producto != 'producto'
GROUP BY producto;