# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                                        songplay_id SERIAL,
                                                        start_time TIMESTAMP REFERENCES time(start_time),
                                                        user_id VARCHAR(50) REFERENCES users(user_id),
                                                        level VARCHAR(10),
                                                        song_id VARCHAR(50) REFERENCES songs(song_id),
                                                        artist_id VARCHAR(50) REFERENCES artists(artist_id),
                                                        session_id BIGINT,
                                                        location VARCHAR,
                                                        user_agent VARCHAR,
                                                        PRIMARY KEY (songplay_id)
                                                        )""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                                                    user_id VARCHAR(50),
                                                    first_name VARCHAR,
                                                    last_name VARCHAR,
                                                    gender VARCHAR(1),
                                                    level VARCHAR(10),
                                                    PRIMARY KEY (user_id)
                                                    )""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                                                    song_id VARCHAR(50),
                                                    title VARCHAR,
                                                    artist_id VARCHAR(50),
                                                    year INT,
                                                    duration FLOAT,
                                                    PRIMARY KEY (song_id)
                                                    )""")


artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                                                        artist_id VARCHAR(50),
                                                        name VARCHAR,
                                                        location VARCHAR,
                                                        latitude FLOAT,
                                                        longitude FLOAT,
                                                        PRIMARY KEY (artist_id)
                                                        )""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                                                    start_time TIMESTAMP,
                                                    hour INT,
                                                    day INT,
                                                    week INT,
                                                    month INT, 
                                                    year INT,
                                                    weekday VARCHAR,
                                                    PRIMARY KEY (start_time)
                                                    )""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """)

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET first_name=users.first_name, last_name=users.last_name, gender=users.gender, level=users.level """)

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO UPDATE SET title=songs.title, artist_id=songs.artist_id, year=songs.year, duration=songs.duration """)

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO UPDATE SET name=artists.name, location=artists.location, latitude=artists.latitude, longitude=artists.longitude """)

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO UPDATE SET hour=time.hour, day=time.day, week=time.week, month=time.month, year=time.year, weekday=time.weekday """)

# FIND SONGS

song_select = (""" SELECT songs.song_id, artists.artist_id FROM songs, artists WHERE songs.artist_id = artists.artist_id AND songs.title = %s AND artists.name = %s AND songs.duration = %s """)

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]