#%%
# import libraries & packages
from pathlib import Path
import pandas as pd
from sanity_check_function import categories_sanity_check, validate_data_types, missing_values, plot_distribution, plot_histogram


#%%
# Load Data
BASE_DIR = Path(__file__).resolve().parents[2]
#print(BASE_DIR)
FILE_NAME = "raw_data.xlsx"
DATA_PATH = BASE_DIR / "data" / "raw" / FILE_NAME

SHEET_NAME = "Account"
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME)
print(df) 

#%%
# Categories sanity check
categories_sanity_check(df, "Gender", ["Male", "Female"])


#%%
# Data type sanity check
validate_data_types(df, {"Name": "str", 
                         "Gender": "str", 
                         "Age": "int64",
                         "Salary" : "float64",
                         "LocationId": "int64",
                         "Churned": "int64"
                         })




#%%
# Missing values sanity check
missing_values(df)




#%%
# Outliers sanity check
plot_distribution(df, "Tenure")
plot_histogram(df, "Tenure")


#%%
#Dealing with missing values
df['Balance'] = df['Balance'].fillna(df['Balance'].mean())



# %%
#Remove name column
df = df.drop(["AccountId"], axis=1)


# %%
# Export file
OUTPUT_DIR = BASE_DIR / "data" / "processed"
file_name = 'account.csv'
file_path = OUTPUT_DIR / file_name
df.to_csv(file_path, index=False)


# %%
