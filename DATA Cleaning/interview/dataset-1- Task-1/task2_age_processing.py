import pandas as pd

# Load Excel file
file = "DATest_2.xlsx"

# Read sheets
input_df = pd.read_excel(file, sheet_name="Age_Input")
desired_df = pd.read_excel(file, sheet_name="Age_DesiredOutput")

print("Input columns:", input_df.columns)
print("Desired columns:", desired_df.columns)

# ---- Example transformation ----
# If DesiredOutput is grouped data
if len(desired_df) < len(input_df):
    # Try grouping
    result = input_df.groupby("Age")["Income"].mean().reset_index()
    result.columns = desired_df.columns
else:
    result = input_df.copy()

# Save output
result.to_csv("Age_Output.csv", index=False)

print("CSV file created successfully")
