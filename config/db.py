import mysql.connector


def connectDB():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="kp_cisareno"
    )
    return db

