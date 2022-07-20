from config.db import connectDB
from models import pns


class pnsController:
    def __init__(self):
        self.db = connectDB()

    def show_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM pns"
        cursor.execute(sql)
        results = cursor.fetchall()
        datas = []
        if cursor.rowcount < 0:
            return None
        else:
            for idx in results:
                data = pns(idx[0], idx[1], idx[2], idx[3], idx[4])
                datas.append(data)

        return datas

    def show_by_month(self, key):
        cursor = self.db.cursor()
        sql = "SELECT * FROM pns WHERE bulan=%s"
        cursor.execute(sql, key)
        results = cursor.fetchall()
        datas = []
        if cursor.rowcount < 0:
            return None
        else:
            for idx in results:
                data = pns(idx[0], idx[1], idx[2], idx[3], idx[4])
                datas.append(data)

        return datas

    def insert_data():
        pass
