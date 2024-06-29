import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database=''
    )

def fetch_all(query):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def execute_query(query, params=None):
    conn = create_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
