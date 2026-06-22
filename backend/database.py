import sqlite3


def create_database():

    connection = sqlite3.connect("blog.db")

    cursor = connection.cursor()


    # Users table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )
    """)



    # Posts table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        title TEXT NOT NULL,

        content TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # Comments table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        post_id INTEGER,

        user_id INTEGER,

        comment TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    connection.commit()

    connection.close()



if __name__=="__main__":

    create_database()

    print("Database created successfully")
