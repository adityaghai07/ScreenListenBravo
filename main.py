import pandas as pd
from services.db import insert_into_table , check_connection
from services.utils import is_tech_company
import csv
import uvicorn
from fastapi import FastAPI, UploadFile, File
import io



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hey! Aditya this side!"}


@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    content = await file.read()
    csv_data = csv.DictReader(io.StringIO(content.decode('utf-8')))

    db = check_connection()

    try:

        for row in csv_data:
            company_name = row['company_name']
            description = row['Description']
            is_tech = is_tech_company(description)

            print(f"Company: {company_name}, Description: {description}, Is Tech: {is_tech}")
            print("\n\n")
            
            insert_into_table("company", ["company_name", "description", "technology_company"], [company_name, description, is_tech])
        return {"message": "CSV processed and data inserted successfully"}
    
    except Exception as e:
        return {"error": str(e)}
    


# use this command to run the server

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)