import models
import mysql.connector

class App:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="kp_cisareno"
        )
    
        

if __name__ == '__main__':
    pass
