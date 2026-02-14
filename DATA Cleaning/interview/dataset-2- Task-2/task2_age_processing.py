import pandas as pd

# File name
file = "DATest_2.xlsx"
# Read the only sheet
df = pd.read_excel(file, sheet_name="Sheet1")
print("Data loaded")
print(df.head())
# Group by Age and calculate average income
output = df.groupby("Age")["Income"].mean().reset_index()
# Rename column
output.columns = ["Age", "Average_Income"]
# Save as CSV
output.to_csv("Age_Output.csv", index=False)
print("CSV file created successfully")
