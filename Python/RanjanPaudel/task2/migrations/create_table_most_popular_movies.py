import sqlite3

imdb_movies_db = 'sqlite_dbs/imdb_movies.db'


def create_table():
    with sqlite3.connect(imdb_movies_db) as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS most_popular_movies
                            (id INTEGER PRIMARY KEY ASC, 
                            title TEXT, 
                            release_year INTEGER, 
                            imdb_rating TEXT, 
                            position INTEGER, 
                            pre_position INTEGER,
                            popularity TEXT,
                            UNIQUE(title, release_year, position))
                        ''')
        connection.commit()


if __name__ == "__main__":
    create_table()
