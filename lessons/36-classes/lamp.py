# Practice 3 (one answer): a Lamp class that switches on and off
class Lamp:
    def __init__(self, room):
        self.room = room
        self.on = False

    def toggle(self):
        self.on = not self.on


desk = Lamp("office")
desk.toggle()
print(desk.room, "lamp on:", desk.on)
desk.toggle()
print(desk.room, "lamp on:", desk.on)
