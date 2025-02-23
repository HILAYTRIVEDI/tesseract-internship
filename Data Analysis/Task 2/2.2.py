# Remove duplicates from the data set

import pandas as pd

data = pd.read_csv('sample_data.csv')

data.drop_duplicates(inplace=True)

data.to_csv('sample_data.csv', index=False)

print('Duplicates removed successfully')