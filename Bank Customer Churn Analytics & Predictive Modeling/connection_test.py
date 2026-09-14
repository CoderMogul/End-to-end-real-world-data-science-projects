#%%
import sys
print(sys.executable)

#%%
# create the folder path for the virtual environment
from pathlib import Path

folders = [
    "documentation/docs",
    "documentation/figures",

    "data/raw",
    "data/processed",

    "scripts/data_preprocessing",
    "scripts/data_ingestion",

    "eda_queries",

    "notebook/statistical_testing",

    "predictive_modelling/building_models",
    "predictive_modelling/evaluating_models",
    "predictive_modelling/responsible_AI",

    "data_visualization"
] 
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)




#%%
# test pandas in interactive mode
import pandas as pd

data = {
        "customer_id": [1, 2, 3, 4, 5],
        "customer_name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "age": [25, 30, 35, 40, 45],
        "churned": [False, True, False, True, False]

}
df = pd.DataFrame(data)
# %%
