from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse

from routes.utils import select_all_tables, select_one_row  # Import the function from users.py
import uvicorn

app = FastAPI()


@app.get("/select_all_tables/{table_name}")
def select_all_tables_(table_name: str):
    return select_all_tables(table_name)


@app.post("/select_one_row")
def select_one_row_(json: dict):
    return select_one_row(json)

# Swagger UI and ReDoc routes
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(openapi_url="/openapi.json", title="redoc")

@app.get("/openapi.json", include_in_schema=False)
async def openapi_json():
    return JSONResponse(content=get_openapi(title="Your API Title", version="1.0.0", routes=app.routes))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
