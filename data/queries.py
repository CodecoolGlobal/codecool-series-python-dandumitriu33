from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_top_15_shows(offset=0):
    return data_manager.execute_select(f'''
    SELECT title, year, runtime, MIN(genres.name) as genre, rating, trailer, homepage FROM shows 
    JOIN show_genres ON shows.id = show_genres.show_id
    JOIN genres ON show_genres.genre_id = genres.id
    GROUP BY title, year, runtime, rating, trailer, homepage
    ORDER BY rating DESC LIMIT 15 OFFSET {offset};    
    ''')


def get_only_genres_for_top_15(offset=0):
    return data_manager.execute_select(f'''
        SELECT title, rating, genres.name FROM shows
        JOIN show_genres ON shows.id = show_genres.show_id
        JOIN genres ON show_genres.genre_id = genres.id
        GROUP BY title, rating, genres.name
        ORDER BY rating DESC LIMIT 15 OFFSET {offset}
''')
