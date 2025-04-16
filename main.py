from fastapi import FastAPI, UploadFile, File, Form
from pathlib import Path
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5051"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("documents")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/uploadfile/")
async def create_upload_file(
      chantier_id: str = Form(...),
      files: List[UploadFile] = File(...)
    ):
    saved_files = []
    chantier_dir = UPLOAD_DIR / chantier_id
    chantier_dir.mkdir(parents=True, exist_ok=True)
    
    for file in files:
        file_path = chantier_dir / file.filename
        with open(file_path, "wb") as f:
          content = await file.read()
          f.write(content)
        saved_files.append(file.filename)

    return {"chantier_id": chantier_id, "files": saved_files}

@app.get("/listfiles/")
async def list_files(chantier_id: str):
    target_dir = UPLOAD_DIR / chantier_id
    if not target_dir.exists():
        return JSONResponse(content={"files": []})
    
    files = [f.name for f in target_dir.iterdir() if f.is_file()]
    return {"files": files}