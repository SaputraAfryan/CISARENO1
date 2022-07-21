from schemas.apbd import MApbd
from models.apbd import Apbd
from fastapi import APIRouter, Response, status
from config.database import conn

apbd = APIRouter() 

@apbd.get('/apbd/all', response_model=MApbd, 
             description="Menampilkan semua data")
async def find_all_apbd(limit: int = 10, offset: int = 0):
    query = Apbd.select().offset(offset).limit(limit)
    data = conn.execute(query).fetchall()
    response = {"limit": limit, "offset": offset, "data": data }
    return response

@apbd.get('/apbd/{id}',
             description="Menampilkan detail data")
async def find_apbd(id: int, response: Response):
    query = Apbd.select().where(Apbd.c.id == id)
    """
    Kenapa pakai huruf c pada Apbd.c ?
    karena memakai ImmutableColumnCollection
    untuk melihat apa isinya silahkan uncomment print dibawah ini 
    dan lihat di terminal/cmd
    """
    #print(Apbd.c)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "data tidak ditemukan", "status": response.status_code}

    response = {"message": f"sukses mengambil data dengan id {id}", "data": data }
    return response
