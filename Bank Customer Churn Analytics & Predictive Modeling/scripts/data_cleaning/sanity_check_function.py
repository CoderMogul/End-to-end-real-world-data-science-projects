#%%
# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

#%%
# Function: Categories sanity check
def categories_sanity_check(df, column, valid_values):
    invalid = df[~df[column].isin(valid_values)]
    return invalid[column].value_counts()

#%%
# Function: Data type sanity check
def validate_data_types(df, expected_types: dict):
    mismatched_types = {}
    for column, expected_type in expected_types.items():
        if column in df.columns:
            actual_type = df[column].dtype
            if actual_type != expected_type:
                mismatched_types[column] = (actual_type, expected_type)
    return mismatched_types

#%%
# Function: Missing values sanity check
def missing_values(df):
    return (
        df.isnull().sum()
        .to_frame("missing_values")
        .assign(missing_percentage = lambda x: (x["missing_values"] / len(df)) * 100)
        .query("missing_values > 0")
    )

#%%
# Function: Outliers sanity check
def plot_distribution(df, column):
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.show()

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()