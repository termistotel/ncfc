#!/usr/bin/python3

import os
import subprocess
import curses
import sys
import argparse
import shutil
import time

all_dir_data = {}

def get_directory_file_count(path):
    """Gets the number of inodes (files and directories) in the specified directory."""
    result = subprocess.run(['du', '--inodes', '-s', path], stdout=subprocess.PIPE, text=True)
    count = result.stdout.split()[0]
    return int(count)

def rescan_subdirs(path):
    subdirs = []
    try:
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                subdir_path = entry.path
                file_count = get_directory_file_count(subdir_path)
                subdirs.append((subdir_path, file_count))
    except PermissionError:
        pass
    subdirs.sort(key = lambda x: -x[1])
    all_dir_data[path] = subdirs

def get_subdirectories(path):
    """Gets a list of subdirectories and their inode count."""
    if path not in all_dir_data.keys():
        rescan_subdirs(path)

    return all_dir_data[path]

def draw_menu(stdscr, current_row, directory):
    """Draw the directory menu."""
    stdscr.clear()
    subdirs = get_subdirectories(directory)
    stdscr.addstr(0, 0, f"Directory: {directory}")
    stdscr.addstr(1, 0, f"Files/Directories: {get_directory_file_count(directory)}")

    for idx, subdir in enumerate(subdirs):
        subdir_name = os.path.basename(subdir[0])
        file_count = subdir[1]
        try:
            if idx == current_row:
                stdscr.addstr(idx + 3, 0, f"> {subdir_name.replace(':', '.')}/ - {file_count} files", curses.A_BOLD)
            else:
                stdscr.addstr(idx + 3, 0, f"  {subdir_name.replace(':', '.')}/ - {file_count} files")
        except Exception as e:
            pass

    stdscr.refresh()
    return subdirs

def confirm_deletion(stdscr, directory):
    """Prompt user to confirm deletion of the directory."""
    stdscr.clear()
    stdscr.addstr(0, 0, f"Are you sure you want to delete '{os.path.basename(directory)}'?")
    stdscr.addstr(1, 0, "Press 'y' for Yes, 'n' for No, or 'a' for Yes and don't ask anymore.")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key == ord('y'):
            return 'yes'
        elif key == ord('n'):
            return 'no'
        elif key == ord('a'):
            return 'dont_ask'
        else:
            continue

def main(stdscr, start_directory):
    curses.curs_set(0)
    current_row = 0
    directory = start_directory
    ask_confirmation = True
    global all_dir_data

    while True:
        subdirs = draw_menu(stdscr, current_row, directory)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(subdirs) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key == curses.KEY_RIGHT:
            try:
                directory = subdirs[current_row][0]
                current_row = 0
            except:
                pass
        elif key == ord('q'):
            break
        elif key == ord('b') or key == curses.KEY_LEFT:
            new_directory = os.path.dirname(directory)
            if new_directory:
                directory = new_directory
                current_row = 0            

        elif key == curses.KEY_DC:  # Delete key
            if subdirs:
                dir_to_delete = subdirs[current_row][0]
                if ask_confirmation:
                    response = confirm_deletion(stdscr, dir_to_delete)
                else:
                    response = 'yes'

                if response == 'yes':
                    shutil.rmtree(dir_to_delete)
                    all_dir_data = {}
                    # rescan_subdirs(directory)
                elif response == 'dont_ask':
                    shutil.rmtree(dir_to_delete)
                    all_dir_data = {}
                    # rescan_subdirs(directory)
                    ask_confirmation = False

                current_row = 0  # Reset selection to avoid dangling references

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ncfi - NC File Inspector")
    parser.add_argument('directory', nargs='?', default=os.getcwd(), help="Directory to inspect")
    args = parser.parse_args()

    curses.wrapper(main, args.directory)
