import numpy as np
import pandas as pd
# open excel file
data = pd.read_excel("Dataset for Data Analytics.xlsx")
print("Shape :", data.shape)
print("\n Missing Values : \n",data.isnull().sum())

numeric_col = data.select_dtypes(include=["int64","float64"]).columns
categorical_col = data.select_dtypes(include=["object","string"]).columns
# Use median for numeric
for col in numeric_col:
    if data[col].isnull().any():
        median_val = data[col].median()
        data[col] = data[col].fillna(median_val)
        print(f"[CR] Imputed '{col}' with median={median_val}")
# use mode for categorical
for col in categorical_col:
    if data[col].isnull().any() and not data[col].mode().empty:
        mod_val = data[col].mode()[0]
        data[col] = data[col].fillna(mod_val)
        print(f"Imputed '{col}' with mode={mod_val}")
# Remove duplicates
before = len(data)
data = data.drop_duplicates()
removed = before - len(data)
print(f"\n[CR] Removed {removed} duplicate rows. Rows remaining: {len(data)}")
# Standardize format
if 'Data' in data.columns:
    data['Data'] = pd.to_datetime(data['Date'], errors='corec').dt.strftime('%Y-%m-%d')
    print("[CR] Standardized 'Date' column to YYYY-MM-DD")
# Text to Proper case
for col in categorical_col:
    data[col] = data[col].astype(str).str.strip().str.title()
    print(f"[CR] Cleaned text in '{col}': strip + title case")
# numeric precision upto 2 decimal 
data[numeric_col] = data[numeric_col].round(2)
print("[CR] Rounded numeric columns to 2 decimal places")
# Final result
print("/n ----Final Result ----")
print("Missing values:\n", data.isnull().sum())
print("Duplicate rows:", data.duplicated().sum())
print("Data types:\n", data.dtypes)
# Save clean file 
data.to_excel("Cleaned Data.xlsx", index=False)
print("\nCleaned file saved: Cleaned_Dataset.xlsx")

