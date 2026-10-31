# Practice 3, one answer: a Playlist whose __str__ uses its own __len__
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"{self.name}: {len(self)} songs"


trip = Playlist("Road trip", ["Highway", "Sunrise", "Home"])
print(len(trip))
print(trip)
