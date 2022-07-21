from schemas.apbn import MApbn
from models.apbn import Apbn
from fastapi import APIRouter, Response, status
from config.database import conn

apbn = APIRouter() 

@apbn.get('/apbn/all', response_model=MApbn, 
             description="Menampilkan semua data")
async def find_all_apbn(limit: int = 10, offset: int = 0):
    query = Apbn.select().offset(offset).limit(limit)
    data = conn.execute(query).fetchall()
    response = {"limit": limit, "offset": offset, "data": data }
    return response

@apbn.get('/apbn/{id}',
             description="Menampilkan detail data")
async def find_apbn(id: int, response: Response):
    query = Apbn.select().where(Apbn.c.id == id)
    """
    Kenapa pakai huruf c pada Apbn.c ?
    karena memakai ImmutableColumnCollection
    untuk melihat apa isinya silahkan uncomment print dibawah ini 
    dan lihat di terminal/cmd
    """
    #print(Apbn.c)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "data tidak ditemukan", "status": response.status_code}

    response = {"message": f"sukses mengambil data dengan id {id}", "data": data }
    return response
