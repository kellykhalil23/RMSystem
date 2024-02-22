import sqlite3

DB_FILE = "recipe_management.db"  # Database file name

def create_tables():
    try:
        conn = sqlite3.connect(DB_FILE)  # Connect to SQLite database
        cursor = conn.cursor()  # Create cursor object to execute SQL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL,
                category TEXT NOT NULL,
                preparation_time TEXT,
                difficulty_level TEXT,
                tags TEXT,
                cuisine TEXT,
                notes TEXT,
                image_url TEXT,
                chef TEXT
            )
        """)  # Create 'recipes' table with necessary columns
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menus (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """)  # Create 'menus' table with necessary columns
        conn.commit()  # Commit changes to the database
        print("Tables created successfully!")  # Confirmation message
        conn.close()  # Close connection
    except sqlite3.Error as e:
        print(e)  # Print any errors if encountered

if __name__ == "__main__":
    create_tables()  # Call the function to create tables when the script is run

