USE master;
GO

IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'BankChurn')
BEGIN
    -- ALTER DATABASE DataWarehouse SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE BankChurn;
END;
GO

CREATE DATABASE BankChurn;
GO

-- use bank churn database
USE BankChurn;
GO

-- If demographic table exists
IF OBJECT_ID ('demographic', 'U') IS NOT NULL
	  DROP TABLE demographic; 
GO
-- Create Demographic Table
CREATE TABLE demographic(
	CustomerId INT PRIMARY KEY IDENTITY(1,1) ,
	Gender NVARCHAR(10),
	Age INT,
	Salary DECIMAL(8,2),
	LocationId INT,
	Churned BIT
);
GO



-- If account table exists
IF OBJECT_ID ('account', 'U') IS NOT NULL
	  DROP TABLE account; 
GO
-- Create Account Table
CREATE TABLE account(
	CustomerId INT,
	Tenure INT,
	Balance DECIMAL(10,2),
	NumProducts INT,
	HasCreditCard BIT,
	IsActive BIT
);
GO



-- If location table exists
IF OBJECT_ID ('location', 'U') IS NOT NULL
	  DROP TABLE location; 
GO
-- Create Location Table
CREATE TABLE location(
	LocationId INT PRIMARY KEY IDENTITY (1,1),
	Geography NVARCHAR(15)
);
GO

