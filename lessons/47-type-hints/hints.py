# Type hints: what goes in, and what comes out
def add_bonus(damage: int, bonus: int) -> int:
    return damage + bonus


print(add_bonus(10, 5))
print(add_bonus("10", "5"))

hits: list[int] = [12, 7, 30]
bag: dict[str, int] = {"potion": 3, "arrow": 20}
spot: tuple[int, int] = (4, 9)
print(max(hits), bag["arrow"], spot)


def count(bag: dict[str, int], item: str) -> int | None:
    return bag.get(item)


print(count(bag, "arrow"), count(bag, "rope"))
