from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).resolve().parent
    UPLOAD_DIR = BASE_DIR / "documents"
    ORIGINS = "https://gis.jdev.fr"
    # Need same right as servicve user if write into service log file
    # Else, check if targeted file exists or create it
    LOG_FILE="/srv/log/edp-documents.log"