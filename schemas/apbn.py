from pydantic import BaseModel, Field
from typing import List


class ApbnSchema(BaseModel):
    nama: str = Field(...)
    tLahir: str = Field(...)
    jabatan: str = Field(...)
    bulan: str = Field(...)
    img_url: str | None = None


class Apbn(ApbnSchema):
    id: int

# list Apbn API


class MApbn(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[Apbn]
