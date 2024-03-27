from dotenv import load_dotenv
import mysql.connector
import os

# Load environment variables from .env file
load_dotenv()
# Access the environment variables
db_host = os.getenv('db_host')
db_user = os.getenv('db_user')
db_pass = os.getenv('db_password')
db_name = os.getenv('db_name')



print(db_host)
# Database configuration
db_config = {
    'host': db_host,
    'user': db_user,
    'password': db_pass,
    'database': db_name
}

try:
    # Connect to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print('Connected to MySQL database')

        # Perform database operations here
        # For example, you can create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Sample query to fetch data from a table
        cursor.execute('SELECT * FROM flowers.guests')
        rows = cursor.fetchall()

        # Print fetched rows
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL database: {e}')

finally:
    # Close the database connection when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL database connection closed')
