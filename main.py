from typing import Optional
from fastapi import FastAPI, Header, Body, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
import psycopg2
from datetime import datetime
from pydantic import BaseModel
import shutil

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
    name : str=''
    phone_number : str=''
    email : str=''
    ministry : str=''
    department : str=''

@app.post("/submit")
async def create_upload_file(request_body: FormObject={}, template_upload : UploadFile = File(...)):
    # write_file
    file_location = f"request_submitted/{template_upload.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(template_upload.file, file_object)
    date = datetime.now()
    # get_request = (request_body.name, request_body.phone_number, request_body.ministry, request_body.department, request_body.template_upload, date, request_body.email)
    # get_data = query_data("""INSERT INTO public.survey_spm
    #                         ("name", phone_number, ministry, department, template_upload, submit_date, email)
    #                         VALUES( '%s', '%s', '%s', '%s', '%s', '%s');""" % (get_request),False)
    # connection.commit()


