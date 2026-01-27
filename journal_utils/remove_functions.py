import os
BASE_PATH = './journals'

def remove_entry(journal_name, entry_name):
    journal_path = os.path.join(BASE_PATH, journal_name)
    full_path = os.path.join(journal_path, entry_name)
    path_exists = os.path.exists(full_path)
    if path_exists:
        os.remove(full_path)
    else:
        print("No such journal")
        return



def remove_journal(journal_name):
    full_path = os.path.join(BASE_PATH, journal_name)
    if os.path.exists(full_path):
        for i in os.listdir(full_path):
            i_path = os.path.join(full_path, i)
            if os.path.isfile(i_path):
                os.remove(i_path)
        os.rmdir(full_path)
    else:
        print("Journal does not exist")