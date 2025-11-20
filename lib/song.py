class Song:
    count = 0 
    genres = []     
    artists = []    
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        Song.genres.append(self.genre)

    def add_to_artists(self):
        Song.artists.append(self.artist)

    @classmethod
    def get_unique_genres(cls):
        return list(set(cls.genres))

    @classmethod
    def get_unique_artists(cls):
        return list(set(cls.artists))
    
    @classmethod
    def add_to_genre_count(cls):
        latest_genre = cls.genres[-1]
        
        if latest_genre in cls.genre_count:
            cls.genre_count[latest_genre] += 1
        else:
            cls.genre_count[latest_genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        latest_artist = cls.artists[-1]
        
        if latest_artist in cls.artist_count:
            cls.artist_count[latest_artist] += 1
        else:
            cls.artist_count[latest_artist] = 1