import os
from .ascii_art import art


def read_journal(journal_name, entry_name):
    folder_path = r"./journals"
    journal_path = os.path.join(folder_path, journal_name)
    entry_path = os.path.join(journal_path, entry_name)
    if os.path.exists(entry_path):
        with open(entry_path, "r") as entry_name:
            print(entry_name.read())
    else:
        print(f"{entry_path} does not exist")
        return
def search_journals():
    print(art["search"])
    journals = os.listdir("./journals")
    for journal in journals:
        if journal.startswith("."):
            continue
        print(art["break"])
        print(journal)
    journal = input("Enter the journal's name:\n ")
    if os.path.exists("./journals/" + journal):
        entry_name = input("Whats the entry?:\n ")
        read_journal(journal, entry_name)

def main():
    search_journals()

if __name__ == "__main__":
    main()