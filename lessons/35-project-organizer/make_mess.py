# Make a messy test folder
from pathlib import Path

folder = Path("messy_downloads")
folder.mkdir(exist_ok=True)
names = [
    "cat.jpg", "logo.PNG", "notes.txt", "report.pdf",
    "song.mp3", "backup.zip", "budget.xlsx", "draft",
]
for name in names:
    (folder / name).touch()
print("Made", len(names), "test files in", folder)
