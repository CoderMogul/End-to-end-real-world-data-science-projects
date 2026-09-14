#%%
# libraries and packages
from pathlib import Path
import pandas as pd
import pyodbc

#%%
print(pyodbc.drivers())

# ===========================================
# Insert the demographic.csv to sql database
# ===========================================
#%%
# demographic data
BASE_DIR = Path(__file__).resolve().parents[2]
FILE_NAME = "demographic.csv"
DATA_PATH = BASE_DIR / "data" / "processed" / FILE_NAME
df = pd.read_csv(DATA_PATH)


#%%
# create connection to SQL Server
conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-DKLV564\\SQLEXPRESS;"
        "Database=BankChurn;"
        "Trusted_Connection=yes;"
)
# %%
#create a cursor object
cursor = conn.cursor()

#%%
#push demographic.csv into database
cursor.execute("SET IDENTITY_INSERT demographic ON")
conn.commit()

#%%
for index, row in df.iterrows():
    cursor.execute(""" 
    INSERT INTO demographic (
        CustomerId,
        Gender,
        Age,
        Salary,
        LocationId,
        Churned
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    int(row.CustomerId),
    row.Gender,
    int(row.Age),
    float(row.Salary),
    int(row.LocationId),
    int(row.Churned)
    )


conn.commit()
print("Data inserted successfully")



# %%
# =========================================
# Insert the location.csv to sql database
# =========================================

#%%
# location data
BASE_DIR = Path(__file__).resolve().parents[2]
FILE_NAME = "location.csv"
DATA_PATH = BASE_DIR / "data" / "processed" / FILE_NAME
df = pd.read_csv(DATA_PATH)


#%%
# create connection to SQL Server
conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-DKLV564\\SQLEXPRESS;"
        "Database=BankChurn;"
        "Trusted_Connection=yes;"
)
# %%
#create a cursor object
cursor = conn.cursor()

#%%
#push location.csv into database
cursor.execute("SET IDENTITY_INSERT location ON")
conn.commit()

#%%
for index, row in df.iterrows():
    cursor.execute(""" 
    INSERT INTO location (
        LocationId,
        Geography
    )
    VALUES (?, ?)
    """,
    int(row.LocationId),
    row.Geography
    )
    
conn.commit()
print("Data inserted successfully")



# =========================================
# Insert the account.csv to sql database
# =========================================

#%%
# account data
BASE_DIR = Path(__file__).resolve().parents[2]
FILE_NAME = "account.csv"
DATA_PATH = BASE_DIR / "data" / "processed" / FILE_NAME
df = pd.read_csv(DATA_PATH)


#%%
# create connection to SQL Server
conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-DKLV564\\SQLEXPRESS;"
        "Database=BankChurn;"
        "Trusted_Connection=yes;"
)
# %%
#create a cursor object
cursor = conn.cursor()

#%%
#push account.csv into database
#cursor.execute("SET IDENTITY_INSERT account ON")
#conn.commit()

#%%
for index, row in df.iterrows():
    cursor.execute(""" 
    INSERT INTO account (
        CustomerId,
        Tenure,
        Balance,
        NumProducts,
        HasCreditCard,
        IsActive
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    int(row.CustomerId),
    int(row.Tenure),
    float(row.Balance),
    int(row.NumProducts),
    int(row.HasCreditCard),
    int(row.IsActive)
    )
    
conn.commit()
print("Data inserted successfully")

# %%
