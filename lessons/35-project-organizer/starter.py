# Your turn: a Videos folder
# This is organizer.py from the video.
# TODO 1: add a line to TYPES so ".mp4" files go into a folder called
#         "Videos" (the key in lowercase, with its dot).
# TODO 2: in make_mess.py, add "movie.mp4" to the names, and run it.
# TODO 3: run this file with DRY_RUN = True, read every line, and only
#         then set DRY_RUN = False and run it again.
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
        if target.exists():
            print(f"Skipped {file.name}: already in {group}")
        elif dry_run:
            print(f"Would move {file.name} to {group}")
        else:
            (folder / group).mkdir(exist_ok=True)
            file.rename(target)
            print(f"Moved {file.name} to {group}")


def main():
    if not FOLDER.exists():
        print("Can't find", FOLDER)
        return
    organize(FOLDER, DRY_RUN)


if __name__ == "__main__":
    main()
