--STATISTICS OF POINTS
-- Median
WITH tb_subset_median AS(
    SELECT *
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (
        SELECT COUNT(*) % 2 == 0 
        FROM points)
    OFFSET (
        SELECT COUNT(*) /2 
        FROM points)
),

tb_median AS (
    SELECT AVG(qtdPontos) AS Median
    FROM tb_subset_median
),

--1o quantile

tb_subset_1quantile AS (
    SELECT *
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (
        SELECT count(*) % 2 == 0
        FROM points
        )
    OFFSET (
        SELECT COUNT(*) / 4
        FROM points
    )
),

tb_1quantile AS (
    SELECT AVG(qtdPontos) AS "1o quantile"
    FROM tb_subset_1quantile
),

--3o quantile
tb_subset_3quantile AS (
    SELECT *
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (
        SELECT COUNT(*) % 2 == 0
        FROM points
    )
    OFFSET (
        SELECT 3 * COUNT(*) / 4 
        FROM points
    )
),

tb_3quantile AS (
    SELECT AVG(qtdPontos) AS "3o quantile"
    FROM tb_subset_3quantile
),

--Mean
tb_mean AS (
    SELECT AVG(qtdPontos) AS "Mean"
    FROM points
),

--Minimum
tb_minimum AS (
    SELECT min(qtdPontos) AS "Minimum"
    FROM points
),

--Maximum
tb_maximum AS (
    SELECT max(qtdPontos) AS "Maximum"
    FROM points
)

SELECT * FROM tb_maximum, tb_minimum,tb_mean,tb_3quantile, tb_1quantile, tb_median



