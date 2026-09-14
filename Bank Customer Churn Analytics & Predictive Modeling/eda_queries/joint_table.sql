SElECT a.CustomerId,
	   a.Tenure,
	   a.Balance,
	   d.Gender,
	   d.LocationId,
	   l.Geography
FROM account a 
JOIN demographic d ON d.CustomerId = a.CustomerId
JOIN location l ON d.LocationId = l.LocationId