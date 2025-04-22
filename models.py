from pydantic import BaseModel
from typing import List

class UploadResponse(BaseModel):
    chantier_id: str
    files: List[str]

class ListFilesResponse(BaseModel):
    files: List[str]

class DeleteResponse(BaseModel):
    message: str