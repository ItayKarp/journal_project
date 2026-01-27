# Journal Manager

A sleek, CLI-based journal management system featuring **ASCII art**, modular Python architecture, and a clean user interface. This application allows you to create, read, and delete journals and entries organized within a directory structure.

---

## 🚀 Quick Start (Linux/macOS)

If you are on a Unix-based system, you can use this bash script to ensure your environment is set up and launch the app immediately.

```bash
#!/bin/bash

# Define the journal directory
JOURNAL_DIR="./journals"

# Create the directory if it doesn't exist
if [ ! -d "$JOURNAL_DIR" ]; then
    echo "Creating journals directory..."
    mkdir "$JOURNAL_DIR"
fi

# Run the application
echo "Starting Journal Manager..."
python3 main.py
```

---

## 📂 Project Structure

The project is organized into a modular package for better maintainability and clarity. All user-created data is stored in a dedicated root folder.

```text
.
├── main.py                 # App entry point; launches the main menu
├── journals/               # Storage for all created journals and entries
│   └── (Your Journal Folders and .txt files live here)
└── journal_utils/          # Core logic package
    ├── __init__.py         # Package initialization (exports main_menu)
    ├── ascii_art.py        # Visual assets and CLI decorations
    ├── create_functions.py # Logic for creating folders and files
    ├── menus.py            # UI layouts and screen management
    ├── read_journal.py     # Logic for searching and displaying text
    ├── remove_functions.py # Logic for deleting entries and journals
    ├── utils.py            # Controller for user input and navigation
    └── validity.py         # Input sanitization and path validation
```

---

## ✨ Features

* 🎨 **ASCII Art Interface**: Visually distinct headers for every action with custom ASCII art for each menu.
* 📖 **Journal Organization**: Automatically manages a `./journals` directory to keep your entries organized.
* 📝 **Full CRUD Support**:
  * **Create**: Generate new journals (folders) and entries (.txt files) with timestamps.
  * **Read**: Browse existing journals and read specific entries with formatted display.
  * **Delete**: Remove specific entries or entire journals with confirmation prompts.

* 🛡️ **Input Sanitization**: Automatically converts spaces to underscores and validates against illegal characters for file system compatibility.
* ⏰ **Automatic Timestamps**: Each entry automatically records creation time and associated journal information.
* 🔍 **Interactive Search**: Search through journals and entries with an intuitive menu system.
* 🖥️ **Cross-Platform**: Works on Windows, macOS, and Linux with platform-specific screen clearing.

---

## 🎮 Main Menu Options

The application provides six main operations:

1. **New Journal** - Create a new journal (folder)
2. **New Entry** - Add a new entry to an existing journal
3. **Read Journal** - Search and read journal entries
4. **Delete Journal** - Remove an entire journal and all its entries
5. **Delete Entry** - Remove a specific entry from a journal
6. **Exit** - Close the application

---

## 📂 Learning File Handling in Python

This project serves as a practical example of how to interact with a computer's file system using Python's built-in `os` module and `open()` function.

### 1. Path Management

To ensure the app works across different operating systems, the project uses `os.path.join`. This is more robust than manual string concatenation because it handles platform-specific separators (like `/` vs `\`) automatically.

```python
# Example from create_functions.py
full_path = os.path.join(BASE_PATH, file_name)
```

### 2. Creating and Deleting Folders

Working with directories is a core part of this project's logic:

* **Creation**: The `os.mkdir()` function is used to create a new folder when a user starts a new journal.
* **Deletion**: To delete a journal, the project uses `os.listdir()` to loop through all files inside a folder, deletes them individually with `os.remove()`, and then removes the empty directory with `os.rmdir()`.

```python
# Example from remove_functions.py
for i in os.listdir(full_path):
    i_path = os.path.join(full_path, i)
    if os.path.isfile(i_path):
        os.remove(i_path)
os.rmdir(full_path)
```

### 3. Reading and Writing Files

The project uses the "context manager" pattern (`with open(...)`) for safety. This ensures that files are properly closed even if an error occurs.

* **Writing**: In `create_entry`, the file is opened in `"w"` (write) mode with UTF-8 encoding, which creates the file and writes the user's description along with metadata.
* **Reading**: In `read_journal`, the file is opened in `"r"` (read) mode to display the content to the CLI.

```python
# Writing example
with open(entry_path, "w", encoding='utf-8') as entry_name:
    entry_name.write(description)
    entry_name.flush()

# Reading example
with open(entry_path, "r", encoding='utf-8') as entry_file_name:
    print(entry_file_name.read())
```

### 4. Verification and Validation

Before performing actions, the code checks if a file or folder actually exists using `os.path.exists()`. This prevents the program from crashing if a user tries to access a journal that doesn't exist.

```python
# Example from validity.py
journal_path = os.path.exists(full_path)
if not journal_path:
    return False
```

### 5. Input Sanitization

The `validity.py` module implements comprehensive input validation:

* **Illegal Character Check**: Prevents use of special characters that might cause file system issues.
* **Blank Input Check**: Ensures users don't create empty or whitespace-only names.
* **Space Replacement**: Automatically converts spaces to underscores for compatibility.
* **File Extension Handling**: Automatically adds `.txt` extension if not provided.

---

## 🛠️ Running the App

Run the application from the root directory using:

```bash
python main.py
```

### Prerequisites

* Python 3.x
* No external dependencies required (uses only standard library modules)

---

## 📋 Module Breakdown

### `main.py`
Entry point that imports and launches the main menu from `journal_utils`.

### `ascii_art.py`
Contains all ASCII art functions for visual elements:
- `create_journal()` - Welcome screen for new journals
- `art_create_entry()` - Header for entry creation with timestamp
- `remove_journal()` - Danger zone confirmation prompt
- `remove_entry()` - Entry deletion confirmation
- `read_journal()` - Book-style display header
- `exit_app()` - Goodbye message
- `init()` - Welcome screen
- `line_break()` - Visual separator
- `search()` - Loading animation

### `create_functions.py`
Handles creation operations:
- `create_journal()` - Creates new journal directory with validation
- `create_entry()` - Writes new entry file with content

### `menus.py`
Manages all UI screens and user interactions:
- `instructions_menu()` - Displays main menu with current date/time
- `create_journal_menu()` - Workflow for creating journals
- `create_entry_menu()` - Workflow for creating entries
- `read_journal_menu()` - Initiates journal search
- `remove_journal_menu()` - Journal deletion workflow
- `remove_entry_menu()` - Entry deletion workflow
- `exit_menu()` - Cleanup and exit
- `clear_screen()` - Cross-platform screen clearing

### `read_journal.py`
Handles reading and displaying content:
- `display_journals()` - Lists all available journals
- `display_entries()` - Lists entries within a journal
- `read_journal()` - Reads and displays entry content
- `search_journals()` - Interactive search workflow

### `remove_functions.py`
Manages deletion operations:
- `remove_journal()` - Deletes journal and all contents
- `remove_entry()` - Deletes specific entry file

### `utils.py`
Controls application flow:
- `main_menu()` - Main application loop
- `handle_user_input()` - Routes user selections to appropriate menus

### `validity.py`
Input validation and sanitization:
- `validate_input()` - Main validation orchestrator
- `check_illegal()` - Validates against illegal characters
- `check_blank()` - Ensures non-empty input
- `check_journal()` - Verifies journal existence
- `check_file_name_len()` - Validates name length
- `check_file_type()` - Ensures .txt extension

---

## 🔐 Security Features

* Input sanitization prevents directory traversal attacks
* Illegal character filtering protects file system integrity
* Path validation ensures operations stay within journals directory
* Confirmation prompts prevent accidental deletions

---

## 🎯 Future Enhancements

Potential features for future development:
* Search within entry content
* Edit existing entries
* Export journals to different formats
* Tag system for entries
* Entry templates
* Password protection for journals
* Backup and restore functionality

---

## 📝 License

This is an educational project demonstrating Python file I/O operations and CLI application design.