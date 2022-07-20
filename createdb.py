from config.db import connectDB


class CreateDB:
    def __init__(self):
        self.db = connectDB()
        self.tName = ['pns', 'apbd', 'apbn']
        for name in self.tName:
            if self.__check_table_exists(name) == False:
                self.__createTable(name)

    def __createTable(self, name):
        match name:
            case 'pns':
                self.__createTablePNS()
            case 'apbd':
                self.__createTableAPBD()
            case 'apbn':
                self.__createTableAPBN()

    def __createTablePNS(self):
        # pns
        cursor = self.db.cursor()
        sql = """CREATE TABLE pns (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255),
        nip VARCHAR(255),
        jabatan VARCHAR(255),
        tLahir VARCHAR(255),
        bulan VARCHAR(255),
        img_url VARCHAR(255)
      )
      """
        cursor.execute(sql)

    def __createTableAPBD(self):
        # apbd
        cursor = self.db.cursor()
        sql = """CREATE TABLE abpd (
          id INT AUTO_INCREMENT PRIMARY KEY,
          nama VARCHAR(255),
          jabatan VARCHAR(255),
          tLahir VARCHAR(255),
          bulan VARCHAR(255),
          img_url VARCHAR(255)        )
        """
        cursor.execute(sql)

    def __createTableAPBN(self):
        # apbn
        cursor = self.db.cursor()
        sql = """CREATE TABLE apbn (
          id INT AUTO_INCREMENT PRIMARY KEY,
          nama VARCHAR(255),
          jabatan VARCHAR(255),
          tLahir VARCHAR(255),
          bulan VARCHAR(255),
          img_url VARCHAR(255)
        )
        """
        cursor.execute(sql)

    def __check_table_exists(self, table_name):
        results = self.db.cursor()
        results.execute(
            "SHOW TABLES FROM {}".format('kp_cisareno'))
        for name in results:
            if table_name in name:
                return True
        return False


if __name__ == '__main__':
    db = CreateDB()
