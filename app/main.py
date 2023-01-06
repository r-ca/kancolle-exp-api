from fastapi import FastAPI
import sqlite3

app = FastAPI()

exp_dbname = 'exp_table.db'

@app.get("/kanmusu/")
async def read_item(current: int = 1, terget: int = 175):
    connection = sqlite3.connect(exp_dbname)
    cursor = connection.cursor()
    sql_current = 'SELECT exp FROM kanmusu WHERE 30 = level'
    cursor.execute(sql_current);
    return {"cur_lv_exp_test": cursor.fetchall()}

    