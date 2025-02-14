import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define API scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from the JSON key file
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

# Open the Google Sheet by name
sheet = client.open("Sample Sheet").sheet1

# Read data into a Pandas DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

print(df.head())  # Display extracted data
