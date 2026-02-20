# databaseconnection.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="pyuser",
        password="py123",
        database="pypro"
    )