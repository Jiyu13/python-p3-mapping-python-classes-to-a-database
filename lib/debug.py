#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

# ==================================================================
# pip install ipdb
# python debug.py
# Song.create_table() => return None
# confirm table was created, run PRAGMA command:
# CURSOR.execute("PRAGMA table_info(songs)").fetchall()
# => [(0, 'id', 'INTEGER', 0, None, 1), (1, 'name', 'TEXT', 0, None, 0), (2, 'album', 'TEXT', 0, None, 0)]

# ==================================================================
# ipdb> hello = Song("Hello", "25")
# ipdb> hello.save()
# ipdb> despacito = Song("Despacito", "Vida")
# ipdb> despacito.save()
# ipdb> CURSOR.execute("PRAGMA table_info(songs)").fetchall()
#  => [(0, 'id', 'integer', 0, None, 1), (1, 'name', 'text', 0, None, 0), (2, 'album', 'text', 0, None, 0)]

# Create the songs table.
# Create two new song instances.
# Use the save() method to persist them to the database.

# ==================================================================
# Check all records saved in song.py
# ipdb> songs = CURSOR.execute('SELECT * FROM songs')
# ipdb> [row for row in songs]
# => [(1, 'Blinding Lights', 'After Hours')]