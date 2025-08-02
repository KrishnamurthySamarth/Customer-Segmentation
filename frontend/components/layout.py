from dash import html, dcc

def serve_layout():
    return html.Div([
        html.H1("Customer Segmentation"),
        dcc.Dropdown(
            id='clustering-method',
            options=[
                {'label': 'KMeans', 'value': 'kmeans'},
                {'label': 'DBSCAN', 'value': 'dbscan'},
                {'label': 'Agglomerative', 'value': 'agglomerative'},
                {'label': 'OPTICS', 'value': 'optics'},
            ],
            value='kmeans'
        ),
    ])
