from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from . import routes

app = FastAPI(docs_url="/docs", redoc_url="/redoc")
app.include_router(routes.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Popular GitHub Repo Checker",
        version="1.0.0",
        description="A service to determine if a GitHub repository is popular or not.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
