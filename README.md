# File Organizer

A simple Python script that organizes files into folders based on their extensions.

## Features

- Choose which directory to organize.
- View the current extension library.
- Add or update extensions and see the updated library.
- Rename incoming files when a filename already exists.
- Skip directories and unrecognized file types.

## Default Extension Library

| Extension | Folder |
|-----------|-----------|
| `.jpg` | Images |
| `.png` | Images |
| `.mp4` | Videos |
| `.mov` | Videos |
| `.doc` | Documents |
| `.pdf` | Documents |
| `.mp3` | Music |

## Getting Started

Install Python 3 and save the script as `organizer.py`. No additional packages are required.

Run the script:

```bash
python organizer.py
```

If needed, use `python3` instead of `python`.

## How to Use

1. Enter the directory path, such as `~/Downloads`.
2. Review the displayed extension library.
3. Enter `y` to add or update an extension, then provide its destination folder name.
4. Review the updated library and repeat as needed.
5. Enter `n` to begin organizing files.

The script moves files into category folders inside your selected directory. It only organizes files directly inside that directory.

**Note:** Custom extension changes apply only to the current run and are not saved.
