# import sqlite3

# CONN = sqlite3.connect('music.db')
# CURSOR = CONN.cursor()

from config import CONN, CURSOR

class Song:
    
    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.id = None


    
    @classmethod
    def create_table(cls):
        '''
            has classmethod "create_table()" that creates a table "songs" if table does not exist.
            set id to None only for being saved into db, when create new song isntance, don't set its id.
            a song gets an id only when it gets saved into db => insert songs into db.
        '''
        query = """
            create table if not exists songs (
                id integer primary key,
                name text,
                album text
            )
        """

        CURSOR.execute(query)


    def save(self):
        '''
            has instancemethod "save()" that saves a song to music.db.
            create a new row for each new instance,
            no need to insert id into table, id'll be added automatically.
        '''
        query = """
            insert into songs (name, album)
            values (?, ?)
        """
        CURSOR.execute(query, (self.name, self.album))

        # grab the id and assign it to be self.id
        # self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        self.id = CURSOR.lastrowid
        CONN.commit()


    @classmethod
    def create(cls, name, album):
        '''
            has classmethod "create()" that creates a Song instance, saves it, and returns it.
            save new instance to db by calling save() instance method
        '''
        new_song = Song(name, album)
        new_song.save()
        return new_song
