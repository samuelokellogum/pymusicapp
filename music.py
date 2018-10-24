class Song:
    def __init__(self, artist, album, title, track_number):
        self.artist = artist
        self.album = album
        self.title = title
        self.track_number = track_number
        artist.add_song(self)
    
class Album:
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title  = title
        self.year = year
        self.tracks = []
        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist

        track_number = len(self.tracks)
        song = Song(title, artist, self, track_number)
        
        self.tracks.append(song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)


class Playlist:
    def __init__(self, name):
       self.name = name 
       self.songs = []

    def add_song(self, song):
        self.songs.append(song)
    

band = Artist("The 69's")
album = Album("Sami", "We Rock", 1999)
album.add_track("Fuck Yeah")
album.add_track("Holy Grail")
album.add_track("Hell Yeah")

playlist = Playlist("Loving It")

for song in album.tracks:
    playlist.add_song(song)

