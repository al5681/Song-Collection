from Song import Song
import pickle


class SongCollection:
    song_list = []

    def __init__(self):
        self.read_file()

    def read_file(self):
        try:
            with open("songs.pickle", 'rb') as f:
                self.song_list = (pickle.load(f))
        except IOError:
            pass

    def update_file(self):
        pickle_out = open("songs.pickle", "wb")
        pickle.dump(self.song_list, pickle_out)
        pickle_out.close()

    def add_song(self, title, artist_name, year_purchased, category):
        new_song = Song(title, artist_name, year_purchased, category)
        self.song_list.append(new_song)
        self.update_file()
        return new_song

    def delete_song(self, song):
        if song in self.song_list:
            self.song_list.remove(song)
            self.update_file()
            return True
        else:
            return False

    def display_songs(self):
        for songs in self.song_list:
            print(songs)

    def get_song_by_artist(self, artist_name):
        songs_by_artist = []
        for songs in self.song_list:
            if songs.artist_name == artist_name:
                songs_by_artist.append(songs)
        return songs_by_artist

    def get_song_by_title(self, title):
        for songs in self.song_list:
            if songs.title == title:
                return songs

    def get_song_list_len(self):
        return len(self.song_list)

    def get_song_list(self):
        return self.song_list

    def get_song_from_string(self, string):
        for songs in self.song_list:
            if str(songs) == string:
                return songs