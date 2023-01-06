from starlette.exceptions import HTTPException
from fastapi import FastAPI
import sqlite3

app = FastAPI()

exp_dbname = 'exp_table.db'

@app.get("/exp/kanmusu/")
async def read_item(current: int = 1, target: int = 175):

    connection = sqlite3.connect(exp_dbname)
    cursor = connection.cursor()

    sql_current = 'SELECT exp FROM kanmusu WHERE ' + str(current) + ' = level'
    cursor.execute(sql_current)
    current_lv_exp = cursor.fetchone()
    # current_lv_exp = current_lv_exp_list[0]

    sql_target = 'SELECT exp FROM kanmusu WHERE ' + str(target) + ' = level'
    cursor.execute(sql_target)
    target_lv_exp = cursor.fetchone()
    # target_lv_exp = target_lv_exp_list[0]

    require_exp = target_lv_exp[0] - current_lv_exp[0]

    return {"require_exp": str(require_exp)}


    