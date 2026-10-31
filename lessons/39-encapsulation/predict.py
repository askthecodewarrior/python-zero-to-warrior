# Predict first, then run it: what does this print?
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


print("Start")
try:
    office = Thermostat(95)
    print("Made it at", office.temp)
except ValueError as e:
    print("Error:", e)
print("End")
