class PhotoAlbum:
    MAX_PAGE_PHOTOS = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(-(-photos_count//cls.MAX_PAGE_PHOTOS))


    def _search_empty_slot(self):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < self.MAX_PAGE_PHOTOS:
                return page
        else:
            return None


    def add_photo(self, label):
        empty_slot = self._search_empty_slot()
        if empty_slot is not None:
            page = empty_slot
            self.photos[page].append(label)
            return f'{label} photo added successfully on page {page+1} slot {len(self.photos[page])}'
        return 'No more free slots'

    def display(self):
        dash = '-' * 11
        result = [dash]

        for page in self.photos:
            filled_positons = ['[]'] * len(page)
            result.append(' '.join(filled_positons))
            result.append(dash)

        return '\n'.join(result)





album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())