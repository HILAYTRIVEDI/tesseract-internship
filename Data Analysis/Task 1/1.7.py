import pdfplumber
import pandas as pd

pdf_path = "./sample_table.pdf" 

with pdfplumber.open(pdf_path) as pdf:
    table_data = []
    
    for page in pdf.pages:
        tables = page.extract_table()
        if tables:
            table_data.extend(tables)

df = pd.DataFrame(table_data[1:], columns=table_data[0])

print(df.head())
