import os
import sys
import shutil
import json

LOG_FILE = "move_log.json"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Documents": [".doc", ".docx", ".txt"],
    "PDFs": [".pdf"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css"]
}


def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Unknown"


def load_log():
    if not os.path.exists(LOG_FILE):
        return []

    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=4)


def organize(path, dry_run=False):
    moved_files = []
    stats = {}

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if not os.path.isfile(item_path):
            continue

        extension = os.path.splitext(item)[1].lower()
        category = get_category(extension)

        destination_folder = os.path.join(path, category)
        destination_file = os.path.join(destination_folder, item)

        if dry_run:
            print(f"[DRY RUN] {item} -> {category}")
            continue

        os.makedirs(destination_folder, exist_ok=True)

        shutil.move(item_path, destination_file)

        moved_files.append({
            "from": item_path,
            "to": destination_file
        })

        stats[category] = stats.get(category, 0) + 1

        print(f"Moved: {item} -> {category}")

    if not dry_run:
        save_log(moved_files)

        print("\nSummary")
        print("-" * 20)

        for category, count in stats.items():
            print(f"{category}: {count}")


def undo():
    if not os.path.exists(LOG_FILE):
        print("No log file found.")
        return

    log = load_log()

    if not log:
        print("Nothing to undo.")
        return

    for move in reversed(log):

        source = move["to"]
        destination = move["from"]

        if os.path.exists(source):
            os.makedirs(
                os.path.dirname(destination),
                exist_ok=True
            )

            shutil.move(source, destination)

            print(
                f"Restored: "
                f"{os.path.basename(source)}"
            )

    save_log([])

    print("\nUndo completed.")


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python organizer.py <folder_path>")
        print("python organizer.py <folder_path> --dry-run")
        print("python organizer.py --undo")
        return

    if sys.argv[1] == "--undo":
        undo()
        return

    path = sys.argv[1]

    if not os.path.exists(path):
        print("Folder does not exist.")
        return

    dry_run = "--dry-run" in sys.argv

    organize(path, dry_run)


if __name__ == "__main__":
    main()