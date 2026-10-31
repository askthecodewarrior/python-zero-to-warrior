# Your turn (lesson 47): one way to solve it
def make_tag(name: str, level: int) -> str:
    return f"{name} lv {level}"


print(make_tag("Rook", 3))
print(make_tag("Rook", "3"))  # runs, but VS Code underlines "3"
