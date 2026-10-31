# The thermostat checks every new temp
class Thermostat:
    def __init__(self, temp):
        self.temp = temp
        self.mode = "off"

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

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in ("heat", "cool", "off"):
            raise ValueError("mode must be heat, cool or off")
        self._mode = value


home = Thermostat(72)
home.mode = "heat"
print(home.mode)
try:
    home.mode = "fan"
except ValueError as e:
    print("Error:", e)
