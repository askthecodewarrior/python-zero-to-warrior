# Nothing stops a bad temperature
class Thermostat:
    def __init__(self, temp):
        self.temp = temp


home = Thermostat(72)
home.temp = 500
print("Heating to", home.temp)
