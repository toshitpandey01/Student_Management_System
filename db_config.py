import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",            # replace with your MySQL username
        password="toshu", # replace with your MySQL password
        database="student_db"
    )
    return conn