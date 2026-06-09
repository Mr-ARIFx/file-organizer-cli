# File Organizer CLI

A Python command-line tool that automatically organizes files into folders based on file extensions.

## Features

- Organize files by type
- Dry-run mode
- Undo operation
- Statistics summary
- Automatic folder creation

## Usage

Organize files:

```bash
python organizer.py "C:\Users\YourName\Downloads"
```

Preview changes:

```bash
python organizer.py "C:\Users\YourName\Downloads" --dry-run
```

Undo:

```bash
python organizer.py --undo
```