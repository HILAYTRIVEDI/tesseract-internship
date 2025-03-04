import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 🔹 Generate Sample Data (100 samples, 10 features)
np.random.seed(42)
df = pd.DataFrame(np.random.rand(100, 10) * 100, columns=[f'Feature_{i}' for i in range(1, 11)])

# 🔹 Standardize the Data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# 🔹 Initialize Dash App
app = dash.Dash(__name__)

# 🔹 Layout of the Dashboard
app.layout = html.Div([
    html.H1("Interactive PCA Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown to select the number of PCA components
    html.Label("Select Number of Principal Components:"),
    dcc.Slider(id='pca-slider', min=2, max=10, step=1, value=2, marks={i: str(i) for i in range(2, 11)}),
    
    # Graph to show PCA scatter plot
    dcc.Graph(id='pca-graph')
])

# 🔹 Callback to update the PCA visualization dynamically
@app.callback(
    Output('pca-graph', 'figure'),
    Input('pca-slider', 'value')
)
def update_pca(n_components):
    pca = PCA(n_components=n_components)
    df_pca = pca.fit_transform(df_scaled)
    
    # Convert to DataFrame for plotting
    df_pca_final = pd.DataFrame(df_pca, columns=[f'PC{i+1}' for i in range(n_components)])
    
    # Create Scatter Plot of first two principal components
    fig = px.scatter(df_pca_final, x="PC1", y="PC2",
                     title=f"PCA with {n_components} Components",
                     labels={"PC1": "Principal Component 1", "PC2": "Principal Component 2"},
                     template="plotly_dark")

    return fig

# 🔹 Run the Dash App
if __name__ == '__main__':
    app.run_server(debug=True)
