import sqlite3

def connect():
    """
    Function to connect to the sqlite3 database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER,
            isbn INTEGER
            )
        """
    )
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    """
    Function to create new rows in the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(
        """
        INSERT INTO book VALUES (NULL,?,?,?,?)
        """, (title, author, year, isbn)
    )
    conn.commit()
    conn.close()


def view():
    """
    Function to read all data from the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM book
        """
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    """
    Function to search for specific database table rows
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(
        """
        SELECT *
        FROM book
        WHERE title = ?
        OR author = ?
        OR year = ?
        OR isbn = ?
        """, (title, author, year, isbn)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    """
    Function to delete a row in the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(
        """
        DELETE FROM book
        WHERE id = ?
        """, (id,)
    )
    conn.commit()
    conn.close()


def update(id,title, author, year, isbn):
    """
    Function to update a row in the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(
        """
        UPDATE book SET
        title = ?,
        author = ?,
        year = ?,
        isbn = ?
        WHERE id = ?
        """, (title, author, year, isbn, id)
    )
    conn.commit()
    conn.close()


connect()  # Will always run connect function when frontend.py is run
