import os
from .validity import validate_input
from . import ascii_art

BASE_PATH = "./journals"
def display_entries(journal_name):
    journal_path = os.path.join(BASE_PATH, journal_name)
    print("""
        ----------------------------
                        """)
    print("Entries:")
    for i in os.listdir(journal_path):
        if not i.startswith("."):
            i = os.path.splitext(i)[0]
            print((i.replace("_", " ")))
            print("")


def display_journals():
    for i in os.listdir(BASE_PATH):
        if not i.startswith('.'):
            print("Journals:")
            print(i)
            print("")

def read_journal(journal_name, entry_name):
    journal_path = os.path.join(BASE_PATH, journal_name)
    entry_path = os.path.join(journal_path, entry_name)
    if os.path.exists(entry_path):
        with open(entry_path, "r", encoding='utf-8') as entry_file_name:
            ascii_art.read_journal(journal_name)
            print(entry_file_name.read())
            input("Press Enter to continue...")
    else:
        print(f"{entry_name} does not exist")
        return

def search_journals():
    ascii_art.search()
    display_journals()
    journal = input("Enter the journal's name:\n ")
    if os.path.exists("./journals/" + journal):
        display_entries(journal)
        entry_name = input("Whats the entry?:\n ")
        entry_name = validate_input(entry_name)
        if not entry_name:
            return
        if not entry_name.endswith(".txt"):
            entry_name = f'{entry_name}.txt'
        read_journal(journal, entry_name)

def main():
    search_journals()

if __name__ == "__main__":
    main()