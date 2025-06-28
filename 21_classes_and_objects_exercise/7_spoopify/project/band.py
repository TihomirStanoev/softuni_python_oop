class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []


    def add_album(self, album):
        album_for_add = next((al for al in self.albums if al.name == album.name), None)

        if not album_for_add:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'
        return f'Band {self.name} already has {album.name} in their library.'


    def remove_album(self, album_name: str):
        album_for_remove = next((al for al in self.albums if al.name == album_name), None)

        if not album_for_remove:
            return f'Album {album_name} is not found.'

        if album_for_remove.published:
            return f'Album has been published. It cannot be removed.'

        self.albums.remove(album_for_remove)
        return f'Album {album_name} has been removed.'


    def details(self):
        info = [f'Band {self.name}']
        for album in self.albums:
            info.append(album.details())

        return '\n'.join(info)


