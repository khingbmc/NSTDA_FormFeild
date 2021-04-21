from typing import Optional
from fastapi import FastAPI, Header, Body, File, UploadFile, Request, Form
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
import psycopg2
from datetime import datetime
import uvicorn
from pydantic import BaseModel
import shutil
import os


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

connection = psycopg2.connect(user="spmadmin",
                                password="Spm_2021@gbdi!depa",
                                host="202.139.197.37",
                                port="5432",
                                database="spmdb")

def query_data(postgreSQL_select_Query,check=True):
    cursor = connection.cursor()

    cursor.execute(postgreSQL_select_Query)
#     print("Selecting rows from mobile table using cursor.fetchall")
    if check:
        records = cursor.fetchall() 
    #     print("Print each row and it's columns values")
        return records
    if check == 'get':
        records = cursor.fetchone() 
    #     print("Print each row and it's columns values")
        return records

@app.get("/min")
def read_root():
    records = query_data("""SELECT id, "name"
                                FROM "WEB_SURVEY".ministry;  """)
    lst_dict = []
    for i in records:
        lst_dict.append({'name': i[1], 'key':i[0]})
    return lst_dict



@app.get("/dep")
async def read_root(ministry:int = 1):
    records = query_data("""SELECT mini_id, "name"
                                FROM "WEB_SURVEY".department
                                WHERE mini_id = %d;  """ % (ministry))
    lst_dict = []
    for i in records:
        lst_dict.append({'name': i[1], 'key':i[1]})
    return lst_dict

class FormObject(BaseModel):
    name : str
    phone_number : str
    email : str
    ministry : str
    department : str

@app.post("/submit")
async def create_upload_file(name : str = Form(...), phone_number : str = Form(...), email : str = Form(...), ministry : str = Form(...),department : str = Form(...), template_upload : UploadFile = File(...)):
    # write_file
    ministry_name = query_data("""SELECT  "name"
                                FROM "WEB_SURVEY".ministry
                                WHERE id = %d;  """ % (int(ministry)))
    day_path = datetime.now().strftime('%d-%m-%Y')
    if not os.path.exists('request_submitted/'+day_path):
        os.mkdir('request_submitted/'+day_path)

    file_location = f"request_submitted/{day_path}/{template_upload.filename}"

    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(template_upload.file, file_object)

    now_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    ministry_name = ''.join(ministry_name[0])
    get_request = (name, phone_number, email, ministry_name, department, template_upload.filename, now_date)
    get_data = query_data("""INSERT INTO "WEB_SURVEY".survey_spm
                            ("name", phone_number, email, ministry, department, template_upload, submit_date)
                            VALUES( '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (get_request),False)
    
    connection.commit()
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
