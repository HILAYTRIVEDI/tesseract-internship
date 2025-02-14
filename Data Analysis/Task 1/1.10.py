import pandas as pd
import requests
import pdfplumber
import gspread
import dask.dataframe as dd
from sqlalchemy import create_engine
from oauth2client.service_account import ServiceAccountCredentials

# Database connection (MySQL Example)
db_engine = create_engine("mysql+pymysql://user:password@host:3306/local_db")

# Function to load data from CSV
def load_csv(file_path):
    return pd.read_csv(file_path)

# Function to load data from Excel
def load_excel(file_path, sheet_name=0):
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Function to load data from Google Sheets
def load_google_sheets(sheet_name, creds_path):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(credentials)
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Function to extract data from APIs
def load_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    return None

# Function to read large datasets using Dask
def load_large_csv(file_path):
    return dd.read_csv(file_path)

# Function to extract tables from a PDF
def load_pdf_tables(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.extend(table)
    return pd.DataFrame(tables[1:], columns=tables[0]) if tables else None

# Function to load data from SQL
def load_sql_data(query):
    return pd.read_sql(query, db_engine)

# Function to automate ingestion from multiple sources
def automate_ingestion():
    data_sources = {
        "csv_data": load_csv("sample_data.csv"),
        "excel_data": load_excel("sample_data.xlsx"),
        "google_sheets": load_google_sheets("GoogleSheetName", "credentials.json"),
        "api_data": load_api_data("https://api.example.com/data"),
        "large_csv": load_large_csv("large_dataset.csv"),
        "pdf_data": load_pdf_tables("sample_table.pdf"),
        "sql_data": load_sql_data("SELECT * FROM users"),
    }
    
    # Merging all data into a single DataFrame (Example)
    final_data = pd.concat([df for df in data_sources.values() if df is not None], ignore_index=True)
    
    # Store the final data in a database
    final_data.to_sql("final_table", db_engine, if_exists="replace", index=False)

    print("Data Ingestion Completed")

# Run the ingestion pipeline
automate_ingestion()
