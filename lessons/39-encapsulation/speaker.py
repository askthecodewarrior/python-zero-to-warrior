# One answer to practice problem 2
class Speaker:
    def __init__(self, volume):
        self.volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if value < 0 or value > 100:
            raise ValueError("volume must be 0 to 100")
        self._volume = value

    @property
    def is_muted(self):
        return self._volume == 0


box = Speaker(40)
print(box.volume, box.is_muted)
box.volume = 0
print(box.volume, box.is_muted)
try:
    box.volume = 150
except ValueError as e:
    print("Error:", e)
print(box.volume)
