# Practice problem 3, fixed: the setter stores _brightness, and
# percent is read with no parentheses
class Lamp:
    def __init__(self, brightness):
        self.brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if value < 0 or value > 100:
            raise ValueError("brightness must be 0 to 100")
        self._brightness = value

    @property
    def percent(self):
        return str(self._brightness) + "%"


desk = Lamp(60)
print(desk.percent)
