from config.db import connectDB
from models import apbn


class apbnController:
    def __init__(self):
        self.db = connectDB()

    def show_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM apbn"
        cursor.execute(sql)
        results = cursor.fetchall()
        datas = []
        if cursor.rowcount < 0:
            return None
        else:
            for idx in results:
                data = apbn(idx[1], idx[2], idx[3], idx[4], idx[5])
                datas.append(data)

        return datas

    def show_by_month(self, key):
        cursor = self.db.cursor()
        sql = "SELECT * FROM apbn WHERE bulan=%s"
        cursor.execute(sql, key)
        results = cursor.fetchall()
        datas = []
        if cursor.rowcount < 0:
            return None
        else:
            for idx in results:
                data = apbn(idx[1], idx[2], idx[3], idx[4], idx[5])
                datas.append(data)

        return datas

    def insert_data(self, data):
        cursor = self.db.cursor()
        val = (data[1], data[2], data[3], data[4], data[5])
        sql = "INSERT INTO apbn (nama, jabatan, tlahir, bulan, img_url) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, val)
        self.db.commit()