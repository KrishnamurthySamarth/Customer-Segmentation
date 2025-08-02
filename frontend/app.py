import dash
from frontend.components.layout import serve_layout 

def dash_app():
    app = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')
    app.layout = serve_layout()
    return app
