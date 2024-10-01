import sqlite3


def createTable():
    # Open connection and cursor using a context manager
    with sqlite3.connect("mydb.db") as conn:
        cursor = conn.cursor()
        # Create users table if it does not exist
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users
                     (name text, email text, message text)"""
        )
        conn.commit()  # Commit the transaction
    print("Table created successfully")


def insertQuery(name, email, message):
    # Ensure table exists before inserting data
    createTable()

    # Open connection and cursor using a context manager
    with sqlite3.connect("mydb.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, message) VALUES (?, ?, ?)",
            (name, email, message),
        )
        print("Inserted:", name, email, message)
        conn.commit()  # Commit the transaction
    print("Data inserted successfully")


if __name__ == "__main__":
    createTable()
