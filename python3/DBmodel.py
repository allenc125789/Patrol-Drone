import mariadb
import sys

try:
    # connection parameters
    conn_params = {
        'user' : "drone",
        'password' : "",
        'host' : "127.0.0.1",
        'port' : 3306,
        'database' : "droneDB"
    }

    # establish a connection
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print(cursor)
