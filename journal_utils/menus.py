import sys
import os
from .read_journal import search_journals,display_journals,display_entries
from . import ascii_art
from .create_functions import create_entry, create_journal
from .remove_functions import remove_entry, remove_journal
from .validity import validate_input, check_journal, check_file_type, check_file_name_len
from datetime import datetime

BASE_PATH = './journals'

def get_journal_name():
    while True:
        display_journals()
        journal_name = input("Enter journal name: ")
        if not check_journal(journal_name):
            print("Journal doesnt exist.")
            journal_name = input("Enter journal name: ")
        if check_journal(journal_name):
            return journal_name




def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def entry_form(journal_name, entry_name):
    current_time =datetime.now()
    description = input("Enter content:\n")
    description = f"""
    Time of usage: {current_time}
    Current Journal: {journal_name}
    Current Entry: {entry_name}
    {description}
    """
    return description

def create_entry_menu(journal_name = None):
    clear_screen()
    if journal_name is None:
        journal_name = get_journal_name()
    if not check_file_name_len(journal_name):
        return
    journal_path = os.path.join(BASE_PATH, journal_name)
    ascii_art.art_create_entry(journal_name)
    file_name = check_file_type()
    if not file_name:
        return
    file_name = validate_input(file_name)
    if not file_name:
        return
    description = entry_form(journal_name, file_name)
    create_entry(file_name, description, journal_path)

def remove_journal_menu():
    clear_screen()
    display_journals()
    file_name = input("Enter the name of the journal you want to remove.\n")
    file_name = validate_input(file_name)
    if not file_name:
        return
    if not ascii_art.remove_journal(file_name):
        print("Wrong journal name.")
        return
    remove_journal(file_name)


def remove_entry_menu():
    clear_screen()
    display_journals()
    journal_name = input("Enter the name of the journal you want to remove an entry in.\n")
    journal_name = validate_input(journal_name)
    if not journal_name:
        return
    entry_name = input("Enter entry name:\n ")
    entry_name = f"{entry_name}.txt"
    entry_name = validate_input(entry_name)
    if not entry_name:
        return
    if not ascii_art.remove_entry(entry_name):
        print("Wrong entry name.")
        return
    remove_entry(journal_name, entry_name)


def read_journal_menu():
    clear_screen()
    search_journals()


def create_journal_menu():
    clear_screen()
    ascii_art.create_journal()
    journal_name = input("Enter journal name: \n")
    if len(journal_name) > 100:
        print("Journal name too long.")
        return False
    journal_name = validate_input(journal_name)
    if not journal_name:
        return True
    if not create_journal(journal_name):
        return False
    return journal_name


def exit_menu():
    clear_screen()
    ascii_art.exit_app()
    sys.exit()


def instructions_menu():
    current_time = datetime.now()
    date_str = current_time.strftime("%b %d, %Y")
    time_str = current_time.strftime("%H:%M")
    print(fr"""
 __________________________________________
|                                          |
|   JOURNAL MANAGER                        |
|   ____________________________________   |
|                                          |
|    1. New Journal       [ DATE ]         |
|    2. New Entry         {date_str}     |
|    3. Read Journal                       |
|    4. Delete Journal    [ TIME ]         |
|    5. Delete Entry      {time_str}            |
|    6. Exit                               |
|   ____________________________________   |
|                                          |
|   SELECT OPTION :   """)


if __name__ == "__main__":
    create_journal_menu()