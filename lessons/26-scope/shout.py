# Practice 3: inner reads name from the enclosing function
def greet_loud(name):
    def shout():
        print(name.upper() + "!")

    shout()


greet_loud("Ana")
