import mysql.connector

def main():
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'employees',
        'raise_on_warnings': True,
        }

    cnx = mysql.connector.connect(**config)

    cnx.close()

