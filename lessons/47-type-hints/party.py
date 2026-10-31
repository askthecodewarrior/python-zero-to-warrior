# Practice 2: a list and a dictionary, each with a hint
party: list[str] = ["Rook", "Ivy", "Max"]
gold: dict[str, int] = {"Rook": 40, "Ivy": 25, "Max": 10}


def total_gold(names: list[str], purse: dict[str, int]) -> int:
    return sum(purse[name] for name in names)


print(total_gold(party, gold))
