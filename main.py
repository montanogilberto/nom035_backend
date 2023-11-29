from fastapi import FastAPI
from routes.utils import select_all_tables, select_one_row  # Import the function from users.py
import uvicorn

app = FastAPI()


@app.get("/select_all_tables/{table_name}")
def select_all_tables_(table_name: str):
    return select_all_tables(table_name)


@app.post("/select_one_row")
def select_one_row_(json: dict):
    return select_one_row(json)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
