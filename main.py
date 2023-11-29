from fastapi import FastAPI
from routes.utils import select_all_tables, select_one_row  # Import the function from users.py
import uvicorn

app = FastAPI()

@app.exception_handler(Exception)
async def error_handler(request, exc):
    return {"detail": f"An error occurred: {exc}"}

@app.get("/select_all_tables/{table_name}")
def select_all_tables_(table_name: str):
    try:
        return select_all_tables(table_name)
    except Exception as e:
        raise e  # Propagate the exception to the global error handler

@app.post("/select_one_row")
def select_one_row_(json: dict):
    try:
        return select_one_row(json)
    except Exception as e:
        raise e  # Propagate the exception to the global error handler

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
