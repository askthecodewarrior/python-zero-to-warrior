# Your turn (lesson 47): give make_tag type hints
# TODO 1: name is a str, level is an int, and it returns a str
def make_tag(name, level):
    return f"{name} lv {level}"


print(make_tag("Rook", 3))
# TODO 2: call make_tag with the level in quotes, like "3",
#         and look for the squiggle (Type Checking Mode: basic)
