from config import CONN, CURSOR


class Song:
    
    # 1. initialise name and album attributea
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
        
    
    # 2. create class method to create 'songs' table
    # give table column names that match the attributes of each instance
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)


    # 4. cerate insert statement to insert data into song able
    # use name and album to create a new row in songs table
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        # cursor.execute(query, params_for_query)

        # 5. Grab the id, assign it to the id of the associtated db table row
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        
        CONN.commit()


    # 6. create() cls method to instantialise new instance 
    # and save it automatically to database
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song


# 3. create instances save pass in arg into self.name and self.album
# blinding_lights = Song("Blinding Lights", "After Hours")
# blinding_lights.name
# blinding_lights.album

# # 4. save the created instance to database
# blinding_lights.save()


# 6. use create() classmethod, don't need to save the instance every time an instance is created
# new_song = Song.create("name", "album")
