'''
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
'''
import os

def list_directory_contents(path):
    # Try to list and print all files and subdirectories in the given path
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except NotADirectoryError:
        print(f"{path} is not a directory.")
    except PermissionError:
        print(f"You do not have permissions to access the directory {path}.")

# Prompt the user for the directory path
dir_path = input("Please enter the directory path: ")
list_directory_contents(dir_path)
