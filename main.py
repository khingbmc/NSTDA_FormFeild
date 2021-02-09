from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
import psycopg2
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
connection = psycopg2.connect(user="postgresadmin",
                                password="12345678",
                                host="db-spm.can6o4phsaje.ap-southeast-1.rds.amazonaws.com",
                                port="5432",
                                database="postgres")
def query_data(postgreSQL_select_Query):
    cursor = connection.cursor()

    cursor.execute(postgreSQL_select_Query)
#     print("Selecting rows from mobile table using cursor.fetchall")
    records = cursor.fetchall() 
#     print("Print each row and it's columns values")
    return records

@app.get("/min")
def read_root():
    records = query_data("""SELECT id, "name"
                                FROM public.ministry;  """)
    lst_dict = []
    for i in records:
        lst_dict.append({'name': i[1], 'key':i[0]})
    return lst_dict



@app.get("/dep")
async def read_root(ministry:int = 1):
    records = query_data("""SELECT mini_id, "name"
                                FROM public.department
                                WHERE mini_id = %d;  """ % (ministry))
    lst_dict = []
    for i in records:
        lst_dict.append({'name': i[1], 'key':i[1]})
    return lst_dict