# Practice 1: say how many files it moved (or would move)
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
    count = 0
    for file in sorted(folder.iterdir()):
        if file.is_dir():
            continue
        group = folder_for(file)
        target = folder / group / file.name
        if target.exists():
            print(f"Skipped {file.name}: already in {group}")
        elif dry_run:
            print(f"Would move {file.name} to {group}")
            count += 1
        else:
            (folder / group).mkdir(exist_ok=True)
            file.rename(target)
            print(f"Moved {file.name} to {group}")
            count += 1
    if dry_run:
        print("Would move", count, "files")
    else:
        print("Moved", count, "files")


def main():
    if not FOLDER.exists():
        print("Can't find", FOLDER)
        return
    organize(FOLDER, DRY_RUN)


if __name__ == "__main__":
    main()
