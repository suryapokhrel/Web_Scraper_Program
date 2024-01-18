# utils/database.py
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    mysql_config = {
        "host": "localhost",
        "user": "surya",
        "password": "imsurya@10",
        "database": "selenium",
    }

    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        return conn, cursor
    except Error as err:
        print(f"Error: {err}")
        exit(1)

def create_table_if_not_exists(cursor, module_name):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {module_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bid_hash VARCHAR(64) UNIQUE NOT NULL,
        bid_number VARCHAR(255) NOT NULL,
        bid_description TEXT,
        bid_link VARCHAR(255),
        ECGAINS VARCHAR(255),
        module_name VARCHAR(255),
        due_date VARCHAR(255),
        attachment_path VARCHAR(255),
        file_name VARCHAR(255),
        file_size VARCHAR(25),
        base_url VARCHAR(255)
    );
    """

    try:
        cursor.execute(create_table_query)
        connect_to_database.conn.commit()
    except Error as err:
        print(f"Error creating table: {err}")
        exit(1)

def insert_data_into_table(cursor, conn, module_name, bid_hash, bid_id, description, base_url, download_link, ecgains, due_date, attachment_path, file_name, size_str):
    insert_query = f"""
    INSERT INTO {module_name} (bid_hash, bid_number, bid_description, base_url, bid_link, ECGAINS, module_name, due_date, attachment_path, file_name, file_size)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(insert_query, (bid_hash, bid_id, description, base_url, download_link, ecgains, module_name, due_date, attachment_path, file_name, size_str))
        conn.commit()
        print(f"Data inserted for bid ID: {bid_id}")
    except Error as err:
        print(f"Error inserting data: {err}")
