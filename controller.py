import connector as db


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def ShowPns(self, model):
        cursor = db.cursor()
        sql = f"SELECT * FROM pns WHERE month = (exact month)"
        cursor.execute(sql)
        results = cursor.fetchall()

        if cursor.rowcount < 0:
            print("Tidak ada data")
        else:
            print(results)
