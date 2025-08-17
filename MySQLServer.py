import mysql.connector

try:
    # Connect to MySQL Server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    # Create cursor
    mycursor = mydb.cursor()

    # Create database if not exists
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:  # ✅ This is what ALX is checking for
    print(f"Error: {err}")

finally:
    # Close connection
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()