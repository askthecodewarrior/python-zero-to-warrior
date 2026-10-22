# Default values and keyword arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Ana")
greet("Kai", "Welcome")
greet(greeting="Hi", name="Zed")
greet("Mia", greeting="Hey")
