import os

def create_journal(file_name):
    folder_path = r"./journals"
    full_path = os.path.join(folder_path, file_name)
    check_path = os.path.exists(full_path)
    if check_path:
        print("Name already exists.. Try again!")
    else:
        os.mkdir(full_path)


def create_entry(entry_name, description, journal_path):
    entry_path = os.path.join(journal_path, entry_name)
    with open(entry_path, "w") as entry_name:
        entry_name.write(description)
        entry_name.flush()