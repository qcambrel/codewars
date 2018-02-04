## Kata: I Liked the SQL Better...

# Create an SQLite3 database /tmp/movies.db

# Your database should have a table named MOVIES that contains the following data:

# Name								Year	Rating
# Rise of the Planet of the Apes	2011	77
# Dawn of the Planet of the Apes	2014	91
# Alien								1979	97
# Aliens							1986	98
# Mad Max							1979	95
# Mad Max 2: The Road Warrior		1981	100
# In Haskell, both of the persistent and esqueleto modules are available...

# You will be expected to create a monadic action mkMoviesDB :: IO ()

import sqlite3

def create_movie_database(path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("""CREATE TABLE MOVIES
				 (Name text, Year text, Rating text)""")
	movies = [('Rise of the Planet of the Apes', '2011', '77'),
			  ('Dawn of the Planet of the Apes', '2014', '91'),
			  ('Alien', '1979', '97'),
			  ('Aliens', '1986', '98'),
			  ('Mad Max', '1979', '95'),
			  ('Mad Max 2: The Road Warrior', '1981', '100')]
	c.executemany("INSERT INTO MOVIES VALUES (?, ?, ?)", movies)
	data = [row for row in c.execute("SELECT * FROM MOVIES")]
	conn.commit()
	conn.close()
	return data

if __name__ == "__main__":
	expected = [('Rise of the Planet of the Apes', '2011', '77'),
				('Dawn of the Planet of the Apes', '2014', '91'),
				('Alien', '1979', '97'),
				('Aliens', '1986', '98'),
				('Mad Max', '1979', '95'),
				('Mad Max 2: The Road Warrior', '1981', '100')]
	assert create_movie_database("/tmp/movies.db") == expected
