# The thermostat checks every new temp
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
home.temp = 68
print(home.temp, home.celsius)
try:
    home.temp = 500
except ValueError as e:
    print("Error:", e)
print(home.temp)
