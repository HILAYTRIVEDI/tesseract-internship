import pandas as pd  # Importing pandas for data manipulation

# Read a CSV file
csv_file_path = "data.csv"
df_csv = pd.read_csv(csv_file_path)
print("CSV File:\n", df_csv.head())

# Read an Excel file
excel_file_path = "data.xlsx"
df_excel = pd.read_excel(excel_file_path, sheet_name=0)  # Reads the first sheet
print("\nExcel File:\n", df_excel.head())

# Read a JSON file
json_file_path = "data.json"
df_json = pd.read_json(json_file_path)
print("\nJSON File:\n", df_json.head())
