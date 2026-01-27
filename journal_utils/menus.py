import sys
import os
from .read_journal import search_journals
from .ascii_art import art
from .create_functions import create_entry, create_journal
from .remove_functions import remove_entry, remove_journal
from .validity import validate_input, check_journal


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_entry_menu(journal_name = None):
    clear_screen()

    if journal_name is None:
        while True:
            journal_name = input("Enter journal name: ")
            if not check_journal(journal_name):
                print("Journal doesnt exist.")
                journal_name = input("Enter journal name: ")
            if check_journal(journal_name):
                break
    folder_path = r"./journals"
    journal_path = os.path.join(folder_path, journal_name)
    print(art["create_entry"])
    file_name = input("Enter entry name:\n ")
    file_name = f"{file_name}.txt"
    file_name = validate_input(file_name)
    description = input("Enter content:\n")
    create_entry(file_name, description, journal_path)

def remove_journal_menu():
    clear_screen()
    print(art["remove_journal"])
    file_name = input("Enter the name of the journal you want to remove.\n")
    file_name = validate_input(file_name)
    remove_journal(file_name)


def remove_entry_menu():
    clear_screen()
    print(art["remove_entry"])
    journal_name = input("Enter the name of the journal you want to remove an entry in.\n")
    journal_name = validate_input(journal_name)
    entry_name = input("Enter entry name:\n ")
    entry_name = f"{entry_name}.txt"
    entry_name = validate_input(entry_name)
    remove_entry(journal_name, entry_name)


def read_journal_menu():
    clear_screen()
    print(art["read_journal"])
    search_journals()


def create_journal_menu():
    clear_screen()
    print(art["create_journal"])
    journal_name = input("Enter journal name: \n")
    journal_name = validate_input(journal_name)
    create_journal(journal_name)
    return journal_name


def exit_menu():
    clear_screen()
    print(art["exit"])
    sys.exit()


def instructions_menu():
    print(art["init"])
    print("""
    Welcome to the journal manager.
    Would you like to:

    1.Create a journal

    ■━━━━━━━━━━━━━━━━━ ■ ━━━━━━━━━━━━━━━━━■

    2.Create an entry

    ■━━━━━━━━━━━━━━━━━ ■ ━━━━━━━━━━━━━━━━━■

    3.Remove a journal

    ■━━━━━━━━━━━━━━━━━ ■ ━━━━━━━━━━━━━━━━━■

    4.Remove an entry

    ■━━━━━━━━━━━━━━━━━ ■ ━━━━━━━━━━━━━━━━━■

    5.Read a journal

    ■━━━━━━━━━━━━━━━━━ ■ ━━━━━━━━━━━━━━━━━■

    6.Exit
    """)
