import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/ecommerce_sales_raw.csv")

# Check duplicate count before cleaning
duplicates_before = df.duplicated().sum()
print("Duplicates before cleaning:", duplicates_before)

# Remove duplicate rows
df = df.drop_duplicates()

# Check duplicate count after cleaning
duplicates_after = df.duplicated().sum()
print("Duplicates after cleaning:", duplicates_after)

# Check final row count
print("Rows after removing duplicates:", len(df))

# Fill missing discount values with 0
df["Discount"] = df["Discount"].fillna(0)

# Check remaining missing discount values
print("Missing Discount after cleaning:", df["Discount"].isna().sum())

# Standardize gender values
df["Gender"] = df["Gender"].replace({
    "MALE": "Male"
})

print("\nGender values after cleaning:")
print(df["Gender"].value_counts(dropna=False))

# Standardize city values
df["City"] = df["City"].replace({
    "rajshahi": "Rajshahi"
})

# Fill missing city for C011
df.loc[df["Customer_ID"] == "C011", "City"] = "Chattogram"

print("\nCity values after cleaning:")
print(df["City"].value_counts(dropna=False))

# Remove orders with invalid quantity
invalid_quantity = (df["Quantity"] <= 0).sum()
print("\nInvalid quantity rows:", invalid_quantity)

df = df[df["Quantity"] > 0]

print("Rows after removing invalid quantity:", len(df))

# Final data quality check
print("\n--- Final Data Quality Check ---")

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nInvalid quantity rows:", (df["Quantity"] <= 0).sum())

print("\nTotal rows:", len(df))

# Fill missing customer name using Customer_ID
df.loc[
    (df["Customer_ID"] == "C005") & (df["Customer_Name"].isna()),
    "Customer_Name"
] = "Fahim Rahman"

print("\nMissing Customer_Name after cleaning:", df["Customer_Name"].isna().sum())

# Create cleaned data folder
from pathlib import Path

cleaned_folder = Path("data/cleaned")
cleaned_folder.mkdir(parents=True, exist_ok=True)

# Save cleaned dataset
output_file = cleaned_folder / "ecommerce_sales_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)
print("Rows:", len(df))
print("Columns:", len(df.columns))