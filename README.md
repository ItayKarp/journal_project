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

The project is structured as a Python package for better modularity:

* **`main.py`**: The entry point of the application.
* **`journal_utils/`**: The core package containing:
* `ascii_art.py`: Visual assets for the CLI.
* `create_functions.py` & `remove_functions.py`: Logic for file and folder manipulation.
* `menus.py`: UI logic and screen management.
* `read_journal.py`: Logic for searching and displaying entries.
* `validity.py`: Input sanitization and path checking.
* `utils.py`: The main controller that handles user input and navigation.



---

## ✨ Features

* 🎨 **ASCII Art Interface**: Visually distinct headers for every action.
* 📖 **Journal Organization**: Automatically manages a `./journals` directory to keep your entries organized.
* 📝 **Full CRUD Support**:
* **Create**: Generate new journals (folders) and entries (files).
* **Read**: Scan through existing journals and read specific entries.
* **Delete**: Remove specific entries or entire journals.


* 🛠️ **Input Sanitization**: Automatically converts spaces to underscores for file system compatibility.

---

## 📂 Learning File Handling in Python

This project serves as a practical example of how to interact with a computer's file system using Python's built-in `os` module and `open()` function.

### 1. Path Management

To ensure the app works across different operating systems, the project uses `os.path.join`. This is more robust than manual string concatenation because it handles platform-specific separators (like `/` vs `\`) automatically.

### 2. Creating and Deleting Folders

Working with directories is a core part of this project's logic:

* **Creation**: The `os.mkdir()` function is used to create a new folder when a user starts a new journal.
* **Deletion**: To delete a journal, the project uses `os.listdir()` to loop through all files inside a folder to delete them individually with `os.remove()` before finally removing the empty directory with `os.rmdir()`.

### 3. Reading and Writing Files

The project uses the "context manager" pattern (`with open(...)`) for safety. This ensures that files are properly closed even if an error occurs.

* **Writing**: In `create_entry`, the file is opened in `"w"` (write) mode, which creates the file and writes the user's description.
* **Reading**: In `read_journal`, the file is opened in `"r"` (read) mode to display the content to the CLI.

### 4. Verification and Validation

Before performing actions, the code checks if a file or folder actually exists using `os.path.exists()`. This prevents the program from crashing if a user tries to access a journal that doesn't exist.

---

## 🛠️ Running the App

Run the application from the root directory using:

```bash
python main.py

```

Would you like me to help you create a `requirements.txt` file or perhaps add a "Search" feature to look for keywords inside your journal entries?
