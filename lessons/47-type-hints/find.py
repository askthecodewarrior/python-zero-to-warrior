# Practice 3: a value that might not be there
def find_spot(party: list[str], name: str) -> int | None:
    if name in party:
        return party.index(name)
    return None


party = ["Rook", "Ivy", "Max"]
print(find_spot(party, "Ivy"))
print(find_spot(party, "Zed"))
