from schemas.pns import MPns
from models.pns import Pns
from fastapi import APIRouter, Response, status
from config.database import conn

pns = APIRouter() 

@pns.get('/pns/all', response_model=MPns, 
             description="Menampilkan semua data")
async def find_all_pns(limit: int = 10, offset: int = 0):
    query = Pns.select().offset(offset).limit(limit)
    data = conn.execute(query).fetchall()
    response = {"limit": limit, "offset": offset, "data": data }
    return response

@pns.get('/pns/{id}',
             description="Menampilkan detail data")
async def find_pns(id: int, response: Response):
    query = Pns.select().where(Pns.c.id == id)
    """
    Kenapa pakai huruf c pada Pns.c ?
    karena memakai ImmutableColumnCollection
    untuk melihat apa isinya silahkan uncomment print dibawah ini 
    dan lihat di terminal/cmd
    """
    #print(Pns.c)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "data tidak ditemukan", "status": response.status_code}

    response = {"message": f"sukses mengambil data dengan id {id}", "data": data }
    return response
