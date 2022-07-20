from urllib.request import Request
from config.db import connectDB
from models.pns import Pns as pns


class pnsController:
    def __init__(self):
        self.db = connectDB()

    def show_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM pns"
        cursor.execute(sql)
        results = cursor.fetchall()
        datas = []

        for idx in results:
            data = pns(idx[1], idx[2], idx[3], idx[4], idx[5], idx[6])
            datas.append(data)

        response = {
            "status": 200,
            "results": datas
        }

        return response

    def show_by_month(self, key):
        cursor = self.db.cursor()
        sql = f"SELECT * FROM pns WHERE bulan=%s"
        cursor.execute(sql, [key])
        results = cursor.fetchall()
        datas = []

        response = {
            "status":400,
            "results":'Bad Request!'
        }
        
        if cursor.rowcount <= 0:
            response = {
                "status": 404,
                "results": datas
            }
        else:
            for idx in results:
                data = pns(idx[1], idx[2], idx[3], idx[4], idx[5], idx[6])
                datas.append(data)

            response = {
                "status": 200,
                "results": datas
            }

        return response

    def insert_data(self, data):
        cursor = self.db.cursor()
        val = (data[1], data[2], data[3], data[4], data[5], data[6])
        sql = f"INSERT INTO pns (nama, nip, jabatan, tlahir, bulan, img_url) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, val)
        self.db.commit()
