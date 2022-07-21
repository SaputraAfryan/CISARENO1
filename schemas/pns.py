from pydantic import BaseModel, Field
from typing import List


class PnsSchema(BaseModel):
    nama: str = Field(...)
    nip: str = Field(...)
    tLahir: str = Field(...)
    jabatan: str = Field(...)
    bulan: str = Field(...)
    img_url: str | None = None


class Pns(PnsSchema):
    id: int

# list Pns API


class MPns(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[Pns]
