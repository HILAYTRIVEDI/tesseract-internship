import plotly.express as px
import pandas as pd

# Your custom data
tips = [
    {'day': 'Thur', 'total_bill': 10 },
    {'day': 'Thur', 'total_bill': 20 },
    {'day': 'Fri', 'total_bill': 30 },
    {'day': 'Sat', 'total_bill': 40 },
    {'day': 'Sun', 'total_bill': 50 },
    {'day': 'Thur', 'total_bill': 60 },
    {'day': 'Fri', 'total_bill': 70 },
    {'day': 'Sat', 'total_bill': 80 },
    {'day': 'Sun', 'total_bill': 90 },
    {'day': 'Thur', 'total_bill': 100 },
]

# Convert to DataFrame
df = pd.DataFrame(tips)

# Violin plot (no color='sex' since we don’t have gender info in your custom data)
fig = px.violin(df, y='total_bill', x='day', box=True, points='all',
                title='Violin Plot of Total Bill by Day')
fig.show()
