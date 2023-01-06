from starlette.exceptions import HTTPException
from fastapi import FastAPI
import sqlite3

app = FastAPI()

exp_dbname = 'exp_table.db'

@app.get("/exp/kanmusu/")
async def read_item(current: int = 1, target: int = 175):
    
    # 例外対処
    if current <= 0: #currentの値が下限値(1)を下回っている
        raise HTTPException(status_code=400, detail="INVALID_VALUE_FOR_CURRENT_LEVEL")
    
    if target >= 176: #targetの値が上限値(175)を上回っている
        raise HTTPException(status_code=400, detail="INVALID_VALUE_FOR_TARGET_LEVEL")

    if current == target: #currentとtargetで同じ値が指定されている
        raise HTTPException(status_code=400, detail="TARGET_AND_CURRENT_VALUES_ARE_EQUAL")

    if target < current: #targetにcurrent以下の値が指定されている
        raise HTTPException(status_code=400, detail="CURRENT_HAS_A_VALUE_GREATER_THAN_TARGET")

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


    