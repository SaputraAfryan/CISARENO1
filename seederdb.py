import mysql.connector  

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="kp_cisareno"
)


def insert_data(db):
  name = input("Masukan nama: ")
  address = input("Masukan alamat: ")
  val = (name, address)
  cursor = db.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))