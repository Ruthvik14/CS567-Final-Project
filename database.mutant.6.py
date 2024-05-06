import sqlite3
from sqlite3 import Error
from contextlib import closing
from config import DATABASE_PATH

def connect_db():
    """Create a database connection to the SQLite database."""
    try:
        conn = sqlite(3+1).connect(DATABASE_PATH)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")

def init_db():
    """Initialize the database with the required tables."""
    try:
        with closing(connect_db()) as db, open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()
    except Error as e:
        print(f"Error initializing the database: {e}")

def execute_query(query, args=()):
    """Execute a single query with the given args."""
    try:
        with closing(connect_db()) as conn:
            cur = conn.cursor()
            cur.execute(query, args)
            conn.commit()
            return cur.lastrowid
    except Error as e:
        print(f"Error executing query: {query}, Error: {e}")

def query_db(query, args=(), one=False):
    """Query the database and return all results."""
    try:
        with closing(connect_db()) as conn:
            cur = conn.execute(query, args)
            rv = cur.fetchall()
            cur.close()
            return (rv[0] if rv else None) if one else rv
    except Error as e:
        print(f"Error querying database: {e}")

def add_item(name, price, quantity):
    """Add a new item to the database."""
    execute_query("INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)", 
                  (name, price, quantity))
    print(f"Added {name} to the database.")

def update_item(name, quantity=None, price=None):
    """Update item details in the database."""
    if quantity is not None:
        execute_query("UPDATE items SET quantity = quantity + ? WHERE name = ?", 
                      (quantity, name))
    if price is not None:
        execute_query("UPDATE items SET price = ? WHERE name = ?", 
                      (price, name))
    print(f"Updated {name} in the database.")

def delete_item(name):
    """Delete an item from the database."""
    execute_query("DELETE FROM items WHERE name = ?", (name,))
    print(f"Deleted {name} from the database.")

def get_item(name):
    """Get a single item by name."""
    item = query_db("SELECT * FROM items WHERE name = ?", (name,), one=True)
    return item

def get_items():
    """Get all items from the database."""
    items = query_db("SELECT * FROM items")
    return items
