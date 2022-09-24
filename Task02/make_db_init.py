import sqlite3
conn = sqlite3.connect('movies_rating.db')
cursorObj = conn.cursor()
cursorObj.execute("""CREATE TABLE movies (
                        id INTEGER PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        year VARCHAR(255) NOT NULL,
                        genres VARCHAR(255) NOT NULL)""")

cursorObj.execute("""CREATE TABLE ratings (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        movie_id INTEGER NOT NULL,
                        rating INTEGER,
                        timestamp INTEGER NOT NULL)""")

cursorObj.execute("""CREATE TABLE tags (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        movie_id INTEGER NOT NULL,
                        tag VARCHAR(255) NOT NULL,
                        timestamp INTEGER NOT NULL)""")

cursorObj.execute("""CREATE TABLE users (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        gender VARCHAR(255) NOT NULL,
                        register_date DATE NOT NULL,
                        occupation VARCHAR(255) NOT NULL)""")
conn.commit()
