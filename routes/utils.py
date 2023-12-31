from fastapi import FastAPI
from fastapi.responses import JSONResponse
from databases import connection
import json

app = FastAPI()
conn = connection()

def select_all_tables(table_name: str):
    try:
        cursor = conn.cursor()
        cursor.execute("EXEC sp_select_all_tables @table_name = %s", table_name)

        # Fetch the result as a JSON string
        json_result = cursor.fetchone()[0]

        # Parse the JSON string to a Python dictionary
        result = json.loads(json_result)

        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


def select_one_row(jsonfile: dict):
    try:
        cursor = conn.cursor()
        cursor.execute("EXEC sp_select_one_row @pjsonfile = %s", (json.dumps(jsonfile)))

        # Fetch the result as a JSON string
        json_result = cursor.fetchone()[0]

        # Parse the JSON string to a Python dictionary
        result = json.loads(json_result)

        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
