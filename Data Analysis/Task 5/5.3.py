import pandas as pd
import plotly.express as px

# Sample Data
df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D', 'E'],
    'sales': [100, 150, 130, 90, 120],
    'profit': [20, 35, 25, 15, 22],
    'region': ['North', 'South', 'East', 'West', 'North']
})

# 1. Interactive Scatter Plot
fig1 = px.scatter(
    df, x='sales', y='profit', color='region', text='product',
    title='Sales vs Profit by Region',
    size='profit', hover_data=['product']
)
fig1.show()

# 2. Interactive Bar Chart
fig2 = px.bar(
    df, x='product', y='sales', color='region',
    title='Product Sales by Region', text='sales'
)
fig2.update_traces(texttemplate='%{text}', textposition='outside')
fig2.show()

# 3. Interactive Box Plot (useful for distributions)
fig3 = px.box(
    df, x='region', y='profit', color='region',
    title='Profit Distribution by Region'
)
fig3.show()
