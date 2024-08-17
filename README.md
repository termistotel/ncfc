
# **ncfc - Interactive Directory and File Count Inspector**

**ncfc** (NCurses File Counter) is a command-line utility designed to help you interactively explore directories and view the number of files (inodes) they contain. It also allows you to delete directories with a confirmation prompt, making it a handy tool for managing file systems.

## **Features**

- **Interactive Navigation:**
  - Use the arrow keys to navigate through directories.
  - Press `Enter` or `right arrow` to open and explore a selected subdirectory.
  - Press `b` or `left arrow` to return to the parent directory.

- **File Count Display:**
  - Displays the total number of files and subdirectories within each directory.

- **Delete Functionality:**
  - Press the `Delete` key to remove the currently selected directory.
  - A confirmation prompt appears, allowing you to:
    - **`y` (Yes):** Delete the directory.
    - **`n` (No):** Cancel the deletion.
    - **`a` (Yes and don't ask anymore):** Automatically confirm and delete all future selections without additional prompts.

- **Quit the Utility:**
  - Press `q` at any time to exit the utility.

## **Requirements**

- Python 3.x
- `curses` library (included in Python's standard library)
- `du` command (available on Unix-like systems)
- `shutil` library (included in Python's standard library)

## **Installation**

1. **Download or Clone the Repository:**

   You can download the `ncfc.py` script directly or clone the repository using Git:

   ```bash
   git clone https://github.com/termistotel/ncfc.git
   ```

2. **Navigate to the Directory:**

   ```bash
   cd ncfc
   ```

3. **Make the Script Executable:**

   ```bash
   chmod +x ncfc.py
   ```

## **Usage**

- **Inspect the Current Directory:**
  
  ```bash
  ./ncfc.py
  ```

- **Inspect a Specific Directory:**
  
  ```bash
  ./ncfc.py /path/to/directory
  ```

Once the script is running, you can interactively navigate through directories, view the file counts, and manage directories by deleting them with a simple keystroke.

## **Examples**

- **Exploring a Directory:**

  Run `ncfc` to explore the current directory:

  ```bash
  ./ncfc.py
  ```

  Use the arrow keys to move up and down the list of directories. Press `Enter` to dive into a subdirectory.

- **Deleting a Directory:**

  While exploring, press the `Delete` key to prompt for deletion of the selected directory. Confirm by pressing `y` to delete, `n` to cancel, or `a` to delete and suppress further prompts.

## **License**

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.

## **Disclaimer**

Be careful when using the delete functionality, especially when choosing "don't ask anymore." Deletions are permanent and cannot be undone.

This README file provides a comprehensive overview of the **ncfc** project, including how to install, use, and understand its features. It should help users get started quickly and use the tool effectively.
