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


# Connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect({
                'host': db_host,
                'user': db_user,
                'password': db_pass,
                'database': db_name
            }
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Failed to connect to MySQL database")
            return None
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL: {error}")
        return None

# Create a new record in the database
def create_record(connection, firstName, lastName, age, salary):
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO employees (firstName, lastName, age, salary)
            VALUES (%s, %s, %s, %s)
        """
        values = (firstName, lastName, age, salary)
        cursor.execute(insert_query, values)
        connection.commit()
        print("Record created successfully!")
    except mysql.connector.Error as error:
        print(f"Error creating record: {error}")

# Read all records from the database
def read_records(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("No records found")
    except mysql.connector.Error as error:
        print(f"Error reading records: {error}")

# Update a record in the database
def update_record(connection, employee_id, new_salary):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE employees SET salary = %s WHERE id = %s"
        values = (new_salary, employee_id)
        cursor.execute(update_query, values)
        connection.commit()
        print("Record updated successfully!")
    except mysql.connector.Error as error:
        print(f"Error updating record: {error}")

# Delete a record from the database
def delete_record(connection, employee_id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM employees WHERE id = %s"
        values = (employee_id,)
        cursor.execute(delete_query, values)
        connection.commit()
        print("Record deleted successfully!")
    except mysql.connector.Error as error:
        print(f"Error deleting record: {error}")

# Main function to demonstrate CRUD operations
def main():
    # Connect to the database
    connection = connect_to_db()
    if connection:
        # Create a new record
        create_record(connection, 'John', 'Doe', 30, 50000.00)
        
        # Read all records
        read_records(connection)
        
        # Update a record
        update_record(connection, 1, 55000.00)  # Assuming the record with ID=1 exists
        
        # Read all records again after update
        read_records(connection)
        
        # Delete a record
        delete_record(connection, 1)  # Assuming the record with ID=1 exists
        
        # Read all records again after delete
        read_records(connection)
        
        # Close the connection
        connection.close()
        print("MySQL connection closed")

# if __name__ == "__main__":
#     main()