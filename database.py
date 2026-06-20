import os
import mysql.connector

def get_connection():
    """
    Creates and returns a connection to the MySQL database.
    Reads connection parameters from environment variables (commonly set by Railway),
    falling back to local default development credentials if not present.
    """
    host = os.environ.get("MYSQLHOST", "localhost")
    user = os.environ.get("MYSQLUSER", "root")
    password = os.environ.get("MYSQLPASSWORD", "MASHALLAH")
    database = os.environ.get("MYSQLDATABASE", "placement_tracker")
    
    port_str = os.environ.get("MYSQLPORT", "3306")
    port = int(port_str) if port_str.isdigit() else 3306

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
