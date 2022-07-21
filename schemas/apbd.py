from pydantic import BaseModel, Field
from typing import List


class ApbdSchema(BaseModel):
    nama: str = Field(...)
    tLahir: str = Field(...)
    jabatan: str = Field(...)
    bulan: str = Field(...)
    img_url: str | None = None


class Apbd(ApbdSchema):
    id: int

# list Apbd API


class MApbd(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[Apbd]
