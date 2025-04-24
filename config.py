from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).resolve().parent
    UPLOAD_DIR = BASE_DIR / "documents"
    ORIGINS = "https://gis.jdev.fr"
    LOG_FILE="/srv/log/edp-documents.log"