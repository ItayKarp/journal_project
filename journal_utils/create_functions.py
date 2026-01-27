import os
BASE_PATH = './journals'
from .validity import check_journal
def create_journal(file_name):
    journal_name = check_journal(file_name)
    full_path = os.path.join(BASE_PATH, file_name)
    if journal_name:
        print("Name already exists.. Try again!")
        return False
    else:
        os.mkdir(full_path)
        return True


def create_entry(entry_name, description, journal_path):
    entry_path = os.path.join(journal_path, entry_name)
    with open(entry_path, "w", encoding='utf-8') as entry_name:
        entry_name.write(description)
        entry_name.flush()