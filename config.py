from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).resolve().parent
    UPLOAD_DIR = BASE_DIR / "documents"
    ORIGINS = "http://localhost:5051"