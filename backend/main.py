from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from frontend.app import dash_app

app = FastAPI()

front_app = dash_app()
app.mount("/dashboard", WSGIMiddleware(front_app.server))
