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


def get_show_by_id(show_id):
    return data_manager.execute_select(f'''
    SELECT shows.title, year, shows.overview, runtime, trailer, homepage, rating, string_agg(DISTINCT genres.name, ', ') as genres,
            string_agg(DISTINCT actors.name, ', ') as actors,
            string_agg(DISTINCT seasons.title, ', ') as seasons
    FROM shows JOIN show_genres ON shows.id = show_genres.show_id
                JOIN genres ON show_genres.genre_id = genres.id
                JOIN show_characters ON shows.id = show_characters.show_id
                JOIN actors ON show_characters.actor_id = actors.id
                JOIN seasons ON shows.id = seasons.show_id
    WHERE shows.id = {show_id}
    GROUP BY shows.title, year, shows.overview, runtime, trailer, homepage, rating;
''')


def get_first_20_actors():
    return data_manager.execute_select(f'''
    SELECT actors.name, string_agg(CAST(shows.title as text) , '@@') as titles, string_agg(CAST(shows.id as text), '@@@') as ids FROM actors
        JOIN show_characters ON actors.id = show_characters.actor_id
        JOIN shows ON show_characters.show_id = shows.id
        GROUP BY actors.name
        ORDER BY actors.name LIMIT 20;
''')
