# File Organizer CLI

A lightweight Python command-line utility that automatically organizes files into categorized folders based on their file extensions.

## Features

* Automatically organizes files by type
* Creates destination folders automatically
* Supports common file formats
* Dry-run mode for previewing changes
* Undo support for reverting the last organization operation
* Displays organization statistics
* Handles unknown file types

## Supported Categories

| Category  | Extensions                             |
| --------- | -------------------------------------- |
| Images    | .jpg, .jpeg, .png, .gif, .bmp          |
| Videos    | .mp4, .avi, .mkv, .mov                 |
| Documents | .doc, .docx, .txt                      |
| PDFs      | .pdf                                   |
| Archives  | .zip, .rar, .7z                        |
| Code      | .py, .cpp, .c, .java, .js, .html, .css |
| Unknown   | Any unsupported file type              |

## Project Structure

```text
file-organizer-cli/
│
├── organizer.py
├── README.md
├── .gitignore
└── move_log.json
```

## Requirements

* Python 3.8 or higher

Verify your installation:

```bash
python --version
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Mr-ARIFx/file-organizer-cli.git
```

Navigate to the project directory:

```bash
cd file-organizer-cli
```

No additional packages are required.

## Usage

### Organize Files

Organize files in a specific directory:

```bash
python organizer.py "C:\Users\Username\Downloads"
```

### Dry Run Mode

Preview changes without moving any files:

```bash
python organizer.py "C:\Users\Username\Downloads" --dry-run
```

Example output:

```text
[DRY RUN] photo.jpg -> Images
[DRY RUN] report.pdf -> PDFs
[DRY RUN] movie.mp4 -> Videos
```

### Undo Last Operation

Restore files moved during the most recent organization:

```bash
python organizer.py --undo
```

## Example

### Before

```text
Downloads/
├── photo.jpg
├── report.pdf
├── movie.mp4
├── notes.docx
```

### After

```text
Downloads/
├── Images/
│   └── photo.jpg
├── PDFs/
│   └── report.pdf
├── Videos/
│   └── movie.mp4
├── Documents/
│   └── notes.docx
```

## How Undo Works

Every file movement is recorded in a log file.

When the undo command is executed, all moved files are returned to their original locations.

This allows safe testing and recovery from accidental organization.

## Future Improvements

* Duplicate file handling
* Recursive directory scanning
* Custom categories through JSON configuration
* Graphical user interface (GUI)
* Real-time folder monitoring
* Exportable operation reports

## License

This project is released under the MIT License.

## Author

Developed by Arif as a practical Python automation project focused on file management and command-line utilities.
