class Pegawai:
    def __init__(self, nama, nip, jabatan, tempat, tanggal, status):
        self.nama = nama
        self.nip = nip
        self.jabatan = jabatan
        self.tempatLahir = tempat
        self.tglLahir = tanggal
        self.status = status
        
    def insert_data(db):
        name = input("Masukan nama: ")
        address = input("Masukan alamat: ")
        val = (name, address)
        cursor = db.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))
