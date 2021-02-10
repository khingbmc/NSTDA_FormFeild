from typing import Optional
from fastapi import FastAPI, Header, Body, File, UploadFile, Request, Form
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
import psycopg2
from datetime import datetime
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
connection = psycopg2.connect(user="postgresadmin",
                                password="12345678",
                                host="db-spm.can6o4phsaje.ap-southeast-1.rds.amazonaws.com",
                                port="5432",
                                database="postgres")
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
                                FROM public.ministry
                                WHERE id = %d;  """ % (int(ministry)))
    day_path = datetime.now().strftime('%d-%m-%Y')
    if not os.path.exists('request_submitted/'+day_path):
        os.mkdir('request_submitted/'+day_path)

    file_location = f"request_submitted/{day_path}/{template_upload.filename}"

    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(template_upload.file, file_object)

    now_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    ministry_name = ''.join(ministry_name[0])
    get_request = (name, phone_number, ministry_name, department, template_upload.filename, now_date, email)
    get_data = query_data("""INSERT INTO public.survey_spm
                            ("name", phone_number, ministry, department, template_upload, submit_date, email)
                            VALUES( '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (get_request),False)
    
    connection.commit()


