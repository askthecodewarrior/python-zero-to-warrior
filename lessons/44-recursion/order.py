# Predict first: what does this print?
def countdown(n):
    if n == 0:
        print("Go!")
        return
    countdown(n - 1)
    print(n)


countdown(3)
