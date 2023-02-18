from datetime import datetime
import os
from os.path import exists
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import create_db



create_db()

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes import product,category, review

@app.post('/upload')
def uploadImage(file: UploadFile = File(...)):
    newFileName = datetime.utcnow().strftime('%B-%d-%YT%H:%M:%S')+file.filename
    location = 'uploads/'

    with open(location+newFileName, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": newFileName}

@app.get('/upload/{filename}')
def getImage(filename:str):
    path = './uploads/'
    file = exists(path+filename)
    if not file:
        raise HTTPException(status_code=404, detail="image not found")
    else:
        return FileResponse(path+filename)





