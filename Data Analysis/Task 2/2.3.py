# Convert data types (astype, pd.to_datetime).

import pandas as pd

data = pd.read_csv('sample_data.csv')

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])


# Convert the 'price' column to float format
data['price'] = data['price'].astype(float)

