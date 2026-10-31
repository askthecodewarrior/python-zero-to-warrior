# Your turn: give the thermostat a mode
# TODO 1: in __init__, add self.mode = "off" under self.temp = temp
# TODO 2: under celsius, add a mode property that returns self._mode
# TODO 3: add a @mode.setter that raises ValueError unless the value is
#         "heat", "cool" or "off", and otherwise stores it in self._mode
# TODO 4: at the bottom, set home.mode to "heat" and print it, then set it
#         to "fan" inside a try, and print the error
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
class Thermostat:
    def __init__(self, temp):
        self.temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < 50 or value > 90:
            raise ValueError("temp must be 50 to 90")
        self._temp = value

    @property
    def celsius(self):
        return round((self._temp - 32) * 5 / 9, 1)


home = Thermostat(72)
print(home.temp, home.celsius)
