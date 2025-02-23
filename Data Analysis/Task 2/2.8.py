import pandas as pd

# Example dataset with incorrectly formatted dates
data = pd.DataFrame({
    'Date': [
        '2023-10-05',  # Valid
        '10/05/2023',  # Valid but different format
        '05-10-2023',  # Valid but different format
        '2023/10/05',  # Valid but different format
        '2023-13-01',  # Invalid month
        '2023-02-30',  # Invalid day
        'Not a date',  # Invalid format
        None,          # Missing value
    ]
})

print("Original Data:")
print(data)

data['Parsed_Date'] = pd.to_datetime(data['Date'], format='mixed', errors='coerce')

data['Parsed_Date_Filled'] = data['Parsed_Date'].fillna(pd.to_datetime('2023-01-01'))

print("\nParsed Dates (Invalid Dates as NaT):")
print(data[['Date', 'Parsed_Date']])

print("\nParsed Dates with Default Values for Invalid Dates:")
print(data[['Date', 'Parsed_Date_Filled']])
