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

SHEET_NAME = "Location"
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME)
print(df) 




# %%
# Export file
OUTPUT_DIR = BASE_DIR / "data" / "processed"
file_name = 'location.csv'
file_path = OUTPUT_DIR / file_name
df.to_csv(file_path, index=False)


# %%
