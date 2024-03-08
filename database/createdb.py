import sqlite3

DB_FILE = "recipe_management.db"  # Database file name

def create_database():
    try:
        conn = sqlite3.connect(DB_FILE)  # Connect to SQLite database
        print("SQLite Database connected successfully!")  # Confirmation message
        conn.close()  # Close connection
    except sqlite3.Error as e:
        print(e)  # Print any errors if encountered

if __name__ == "__main__":
    create_database()  # Call the function to create the database when the script is run

#