import os
import shutil

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".pdf": "Documents",
    ".mp3": "Music",
}


def show_library():
    print("\nCurrent extension library:")
    for extension, folder in extensions.items():
        print(f"  {extension} → {folder}")
    print()


# Choose a directory
while True:
    user_input = input(
        "Enter directory to clean (e.g. ~/Downloads): "
    ).strip().strip("\"'")

    if not user_input:
        print("Please enter a directory.")
        continue

    directory = os.path.abspath(os.path.expanduser(user_input))

    if os.path.isdir(directory):
        break

    print("Directory not found. Please try again.")

show_library()

# Optionally customize the extension library
while True:
    choice = input(
        "Would you like to add or update an extension? (y/n): "
    ).strip().lower()

    if choice == "n":
        break

    if choice != "y":
        print("Please enter y or n.")
        continue

    extension = input("Enter an extension (e.g. .csv): ").strip().lower()

    if not extension.startswith("."):
        extension = "." + extension

    if extension == "." or any(
        character in extension for character in '/\\:*?"<>| '
    ):
        print("Invalid extension. Please try again.")
        continue

    folder_name = input(
        "Enter the folder name for this extension: "
    ).strip()

    if (
        not folder_name
        or folder_name in {".", ".."}
        or any(character in folder_name for character in '/\\:*?"<>|')
    ):
        print("Please enter a valid single folder name.")
        continue

    extensions[extension] = folder_name
    print(f"\nUpdated: {extension} → {folder_name}")
    show_library()

# Organize files
try:
    filenames = os.listdir(directory)
except OSError as error:
    print(f"Could not read directory: {error}")
    raise SystemExit(1)

moved_count = 0

for filename in filenames:
    file_path = os.path.join(directory, filename)

    if os.path.islink(file_path) or not os.path.isfile(file_path):
        print(f"Skipped {filename}: not a regular file.")
        continue

    # Match longer extensions first, including custom ones like .tar.gz.
    extension = next(
        (
            ext
            for ext in sorted(extensions, key=len, reverse=True)
            if filename.lower().endswith(ext)
        ),
        None,
    )

    if extension is None:
        print(f"Skipped {filename} due to unknown file extension.")
        continue

    folder_name = extensions[extension]
    folder_path = os.path.join(directory, folder_name)

    try:
        if os.path.islink(folder_path):
            print(f"Skipped {filename}: destination folder is a symbolic link.")
            continue

        os.makedirs(folder_path, exist_ok=True)
        destination_path = os.path.join(folder_path, filename)

        # Avoid overwriting an existing file
        name, suffix = os.path.splitext(filename)
        counter = 1

        while os.path.lexists(destination_path):
            new_filename = f"{name}_{counter}{suffix}"
            destination_path = os.path.join(folder_path, new_filename)
            counter += 1

        shutil.move(file_path, destination_path)
        moved_count += 1

        print(
            f"Moved {filename} to {folder_name}/"
            f"{os.path.basename(destination_path)}"
        )

    except OSError as error:
        print(f"Could not move {filename}: {error}")

print(f"\nFile organization completed. Moved {moved_count} file(s).")
