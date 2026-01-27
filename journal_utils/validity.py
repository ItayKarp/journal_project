import os

def validate_input(user_input):
    if " " in user_input:
        user_input = user_input.replace(" ", "_")
    return user_input

def check_journal(journal_name):
    journal_name = validate_input(journal_name)
    folder_path = r"./journals"
    full_path = os.path.join(folder_path, journal_name)
    journal_path = os.path.exists(full_path)
    if journal_path:
        return journal_path
    else:
        return False