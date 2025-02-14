from sqlalchemy import create_engine
import pandas as pd

db_type = "mysql"
username = "your_username"
password = "your_password"
host = "localhost"
port = "3306"
database = "your_database"

engine = create_engine(f"{db_type}://{username}:{password}@{host}:{port}/{database}")

query = "SELECT * FROM your_table"

df = pd.read_sql(query, con=engine)

print(df.head())
