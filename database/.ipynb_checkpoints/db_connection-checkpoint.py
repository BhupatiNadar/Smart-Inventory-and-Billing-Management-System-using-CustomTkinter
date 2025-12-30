import mysql.connector

def create_connection():
    try:
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bhupati",
            database="Smart_invertry_management_system_using_Ctk"
            )
        return conn
    except mysql.connector as err:
        print(f"Error:{err}")
        return None