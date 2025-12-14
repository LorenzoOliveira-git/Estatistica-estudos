--STATISTICS OF PEOPLE

--Tb_users
WITH tb_users AS (
    SELECT idUsuario,
            sum(qtdPontos) AS Sum_points,
            count(*) as Count_transactions
    FROM points
    GROUP BY idUsuario
),

--Tb_transactions
tb_status_transactions AS (
    SELECT min(Count_transactions) AS "Minimum",
    max(Count_transactions) AS "Maximum",
    avg(Count_transactions) AS "Mean"
    FROM tb_users
),

tb_subset_1quantile_transactions AS (
    SELECT *
    FROM tb_users
    ORDER BY Count_Transactions
    LIMIT 1 + (
        SELECT count(*) % 2 == 0
        FROM tb_users
        )
    OFFSET (
        SELECT count(*) /4 
        FROM tb_users
    )
),

tb_1quantile_transactions AS (
    SELECT AVG(Count_transactions) AS "1o quantile"
    FROM tb_subset_1quantile_transactions
),

tb_subset_median_transactions AS (
    SELECT *
    FROM tb_users
    ORDER BY Count_transactions
    LIMIT 1 + (
        SELECT COUNT(*) % 2 == 0
        FROM tb_users
    )
    OFFSET (
        SELECT COUNT(*) / 2
        FROM tb_users
    )
),

tb_median_transactions AS (
    SELECT AVG(Count_transactions) AS "Median"
    FROM tb_subset_median_transactions
),


tb_subset_3quantile_transactions AS (
    SELECT *
    FROM tb_users
    ORDER BY Count_transactions
    LIMIT 1 + (
        SELECT COUNT(*) % 2 == 0
        FROM tb_users
    )
    OFFSET (
        SELECT 3 * COUNT(*) / 4
        FROM tb_users
    )
),

tb_3quantile_transactions AS (
    SELECT AVG(Count_transactions) AS "3o quantile"
    FROM tb_subset_3quantile_transactions
),

tb_transactions AS (
    SELECT 'Transactions' AS "Variable",* FROM tb_status_transactions, tb_1quantile_transactions,tb_median_transactions,tb_3quantile_transactions
),

--Tb_points
tb_status_points AS (
    SELECT min(Sum_points) AS "Minimum",
    max(Sum_points) AS "Maximum",
    avg(Sum_points) AS "Mean"
    FROM tb_users
),

tb_subset_1quantile_points AS (
    SELECT *
    FROM tb_users
    ORDER BY Sum_points
    LIMIT 1 + (
        SELECT count(*) % 2 == 0
        FROM tb_users
        )
    OFFSET (
        SELECT count(*) /4 
        FROM tb_users
    )
),

tb_1quantile_points AS (
    SELECT AVG(Sum_points) AS "1o quantile"
    FROM tb_subset_1quantile_points

),

tb_subset_median_points AS (
    SELECT *
    FROM tb_users
    ORDER BY Sum_points
    LIMIT 1 + (
        SELECT COUNT(*) % 2 == 0
        FROM tb_users
    )
    OFFSET (
        SELECT COUNT(*) / 2
        FROM tb_users
    )
),

tb_median_points AS (
    SELECT AVG(Sum_points) AS "Median"
    FROM tb_subset_median_points

),


tb_subset_3quantile_points AS (
    SELECT *
    FROM tb_users
    ORDER BY Sum_points
    LIMIT 1 + (
        SELECT COUNT(*) % 2 == 0
        FROM tb_users
    )
    OFFSET (
        SELECT 3 * COUNT(*) / 4
        FROM tb_users
    )
),

tb_3quantile_points AS (
    SELECT AVG(Sum_points) AS "3o quantile"
    FROM tb_subset_3quantile_points

),

tb_points AS (
    SELECT 'Points' AS "Variable", * FROM tb_status_points, tb_1quantile_points,tb_median_points,tb_3quantile_points
)

--Final table
SELECT * FROM tb_points
UNION ALL
SELECT * FROM tb_transactions


