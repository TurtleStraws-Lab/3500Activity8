# ORGN: CMPS 3500
# LAB: Activity 08
# NAME: Moises Gonzalez
# DESC: Improved version of filewords.py with clear exception handling

import sys
import os

USAGE = "Usage: word_writer.py FILE_NAME WORD COUNT"

def print_words(file_name, word, count):
    try:
        with open(file_name, 'x') as file_obj:
            for _ in range(count):
                file_obj.write(word + "\n")
    except FileExistsError:
        print(f"The file {file_name} already exists in this folder.")
        print(USAGE)
    except (PermissionError, OSError):
        print("Invalid file path or permission denied.")
        print(USAGE)

def main():
    try:
        if len(sys.argv) != 4:
            raise IndexError

        file_name = sys.argv[1]
        word = sys.argv[2]

        try:
            count = int(sys.argv[3])
        except ValueError:
            print(f"'{sys.argv[3]}' cannot be converted to an integer.")
            print(USAGE)
            return

        print_words(file_name, word, count)

    except IndexError:
        print("Incorrect number of arguments.")
        print(USAGE)

if __name__ == "__main__":
    main()

