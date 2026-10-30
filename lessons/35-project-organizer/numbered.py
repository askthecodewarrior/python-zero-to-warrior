# Practice 2: a name that's taken gets a number, like "notes (1).txt"
from pathlib import Path

FOLDER = Path("messy_downloads")
DRY_RUN = True
TYPES = {
    ".jpg": "Images",
    ".png": "Images",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".mp3": "Music",
    ".zip": "Archives",
}


def folder_for(file):
    return TYPES.get(file.suffix.lower(), "Other")


def organize(folder, dry_run):
    for file in sorted(folder.iterdir()):
        if file.is_dir():
            continue
        group = folder_for(file)
        target = folder / group / file.name
        n = 1
        while target.exists():
            target = folder / group / f"{file.stem} ({n}){file.suffix}"
            n += 1
        if dry_run:
            print(f"Would move {file.name} to {group} as {target.name}")
        else:
            (folder / group).mkdir(exist_ok=True)
            file.rename(target)
            print(f"Moved {file.name} to {group} as {target.name}")


def main():
    if not FOLDER.exists():
        print("Can't find", FOLDER)
        return
    organize(FOLDER, DRY_RUN)


if __name__ == "__main__":
    main()
