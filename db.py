import mysql.connector
from mysql.connector import Error
import os


def db_conn():

    try:
        connection_config_dict = {
            'user': os.getenv('DB_PROD_USER'),
            'password': os.getenv('DB_PROD_PASSWORD'),
            'host': os.getenv('DB_PROD_HOST'),
            'database': 'Binance',
            'raise_on_warnings': True,
            'use_pure': True,
            'autocommit': True,
            'pool_size': 5,
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)

            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
