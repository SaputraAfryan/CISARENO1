import mysql.connector  
import os

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="toko_mainan"
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


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("pilih id customer> ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("pilih id customer> ")
  sql = "DELETE FROM customers WHERE customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)