 -- Q1: Which customer profiles have the highest churn risk rate by gender

 WITH 
	MainTable AS(
	 SELECT
		[Gender],
		COUNT(*) AS TotalCustomer,
		SUM(CAST([Churned] AS INT)) AS TotalChurn
	FROM [dbo].[demographic]
	GROUP BY [Gender]
	)

SELECT *,
	FORMAT((TotalChurn * 100 /TotalCustomer), 'N1') + '%' AS ChurnRate
FROM MainTable



-- ----------------------------------------------------------------------------
-- Q2: How does churn rate vary across customer segments within each geography.

WITH MainTbl AS (
    SELECT 
        d.Gender,
		CASE
			WHEN d.Age < 30 THEN 'Below 30'
			WHEN d.Age BETWEEN 30 AND 50 THEN 'Between 30 - 50'
			ELSE 'Above 50'
		END AS AgeBracket,
        d.LocationId,
        l.Geography AS Country,
        d.Churned
    FROM demographic d
    JOIN location l ON d.LocationId = l.LocationId),
	
	-- Second CTE
	SecondTbl AS (
		SELECT 
		Country, AgeBracket,
		COUNT(*) AS TotalCustormer,
		AVG(CAST(Churned AS FLOAT)) AS AvgChurnRate,
		AVG(AVG(CAST(Churned AS FLOAT))) OVER(PARTITION BY Country) AS AvgChurnCountry
	FROM MainTbl
	GROUP BY Country, AgeBracket
	)

SELECT *,
	AvgChurnCountry - AvgChurnRate AS Diff
FROM SecondTbl



-- ------------------------------------------------------------------------------------------------
-- Q3: How does churn behavior change when we dynamically slice customers by business parameters ?

DECLARE @MinTenure INT = 8;
DECLARE @MaxBalance DECIMAL = 120000;
DECLARE @MaxProduct INT = 6 

SELECT 
	a.CustomerId,
	a.Tenure,
	a.Balance,
	a.NumProducts,
	d.Churned

FROM account a 
JOIN demographic d ON d.CustomerId = a.CustomerId
WHERE 
	Tenure = @MinTenure
	AND Balance < @MaxBalance
	AND NumProducts < @MaxProduct


SELECT * FROM demographic