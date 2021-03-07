from flask import Flask, request, render_template, redirect, url_for, session

import os
import json
import requests
from dotenv import load_dotenv

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]        

load_dotenv()
secure_creds = {
  "type": "service_account",
  "project_id": os.getenv("project_id"),
  "private_key_id": os.getenv("private_key_id"),
  "private_key": os.getenv("private_key"),
  "client_email": os.getenv("client_email"),
  "client_id": os.getenv("client_id"),
  "auth_uri": os.getenv("auth_uri"),
  "token_uri": os.getenv("token_uri"),
  "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
  "client_x509_cert_url": os.getenv("client_x509_cert_url")
}

with open('confidentials.json', 'w', encoding='utf-8') as f:
    json.dump(secure_creds, f, ensure_ascii=False, indent=4)
    
json_object = json.dumps(secure_creds, indent = 3)

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("FoodFinderDatabase").sheet1

data = sheet.get_all_records()
pprint(data)

row = sheet.row_values(1)
numrows = sheet.row_count - 1 
#print(row)
#olumn = sheet.col_values(1)
#print(column)
#ell = sheet.cell(1,1).value
#rint(cell)




app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route('/')
def your_view():
    sheet = client.open("FoodFinderDatabase").sheet1
    data = sheet.get_all_records()
    numrows = sheet.row_count - 1 
    return render_template('index.html', data = data, numrows = numrows)

if __name__ == "__main__":
  app.run()