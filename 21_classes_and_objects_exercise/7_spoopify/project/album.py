class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)


    def add_song(self, song):
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if song in self.songs:
            return 'Song is already in the album.'

        self.songs.append(song)

        return f'Song {song.name} has been added to the album {self.name}.'


    def remove_song(self, song_name):
        if self.published:
            return 'Cannot remove songs. Album is published.'

        song_for_remove = next((song for song in self.songs if song.name == song_name) , None)

        if song_for_remove:
            self.songs.remove(song_for_remove)
            return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'


    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True

        return f'Album {self.name} has been published.'


    def details(self):
        info = [f'Album {self.name}']
        for song in self.songs:
            info.append(f'== {song.get_info()}')

        return '\n'.join(info)
