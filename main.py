from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from pathlib import Path
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from  config import Config
from fastapi.staticfiles import StaticFiles
import os
from models import UploadResponse, ListFilesResponse, DeleteResponse
import logging

logger = logging.getLogger(__name__)
log_filename = Config.LOG_FILE

logging.basicConfig(filename=log_filename, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[Config.ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Config.UPLOAD_DIR
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

logger.debug(f"Upload directory set to: {UPLOAD_DIR}")

@app.post("/uploadfile")
async def create_upload_file(
      chantier_id: str = Form(...),
      files: List[UploadFile] = File(...)
    ):
    saved_files = []
    chantier_dir = UPLOAD_DIR / chantier_id
    chantier_dir.mkdir(parents=True, exist_ok=True)
    
    for file in files:
        file_path = os.path.join(chantier_dir, file.filename)
        with open(file_path, "wb") as f:
          content = await file.read()
          f.write(content)
          logger.debug(f"Save file: {file_path}")
        saved_files.append(file.filename)

    return UploadResponse(chantier_id=chantier_id, files=saved_files)

@app.get("/listfiles")
async def list_files(chantier_id: str):
    target_dir = UPLOAD_DIR / chantier_id
    if not target_dir.exists():
        return ListFilesResponse(files=[])
    
    files = [f.name for f in target_dir.iterdir() if f.is_file()]
    return ListFilesResponse(files=files)

@app.delete("/deletefile")
async def delete_file(chantier_id: str, filename: str):
    file_path = UPLOAD_DIR / chantier_id / filename
    
    if file_path.exists() and file_path.is_file():
        os.remove(file_path)
        logger.debug(f"Remove file: {filename}")
        return DeleteResponse(message=f"File '{filename}' deleted successfully")
    else:
        logger.debug(f"File not fount: {filename}")
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found")

app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")
