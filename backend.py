import sqlite3

class Database:

    def __init__(self, db):
        """
        Constructor method to connect to the sqlite3 database
        """
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute(
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
        self.conn.commit()


    def insert(self,title,author,year,isbn):
        """
        Method to create new rows in the database
        """
        self.cur.execute(
            """
            INSERT INTO book VALUES (NULL,?,?,?,?)
            """, (title, author, year, isbn)
        )
        self.conn.commit()


    def view(self):
        """
        Method to read all data from the database
        """
        self.cur.execute(
            """
            SELECT *
            FROM book
            """
        )
        rows = self.cur.fetchall()
        return rows


    def search(self,title="",author="",year="",isbn=""):
        """
        Method to search for specific database table rows
        """
        self.cur.execute(
            """
            SELECT *
            FROM book
            WHERE title = ?
            OR author = ?
            OR year = ?
            OR isbn = ?
            """, (title, author, year, isbn)
        )
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        """
        Method to delete a row in the database
        """
        self.cur.execute(
            """
            DELETE FROM book
            WHERE id = ?
            """, (id,)
        )
        self.conn.commit()


    def update(self,id,title, author, year, isbn):
        """
        Method to update a row in the database
        """
        self.cur.execute(
            """
            UPDATE book SET
            title = ?,
            author = ?,
            year = ?,
            isbn = ?
            WHERE id = ?
            """, (title, author, year, isbn, id)
        )
        self.conn.commit()

    def __del__(self):
        """
        Destructor method to close the database connection
        """
        self.conn.close()


