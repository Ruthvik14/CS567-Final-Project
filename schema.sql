-- Create the Categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

DROP TABLE IF EXISTS items;
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    price REAL,
    quantity INTEGER,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

