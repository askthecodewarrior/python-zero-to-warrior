# Practice 3: keep the best score with pathlib
from pathlib import Path

best_file = Path("best.txt")
score = int(input("Your score: "))

if best_file.exists():
    best = int(best_file.read_text())
else:
    best = 0

if score > best:
    best_file.write_text(f"{score}\n")
    print("New best score!")
else:
    print("The best is still", best)
