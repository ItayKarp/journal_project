import os


def remove_entry(journal_name, entry_name):
    folder_path = r"./journals"
    journal_path = os.path.join(folder_path, journal_name)
    full_path = os.path.join(journal_path, entry_name)
    if full_path:
        os.remove(full_path)
    else:
        print("No such journal")
        return



def remove_journal(journal_name):
    folder_path = r"./journals"
    full_path = os.path.join(folder_path, journal_name)
    if os.path.exists(full_path):
        for i in os.listdir(full_path):
            i_path = os.path.join(full_path, i)
            if os.path.isfile(i_path):
                os.remove(i_path)
        os.rmdir(full_path)
    else:
        print("Journal does not exist")