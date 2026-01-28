import os
ILLEGAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '/']
BASE_PATH = './journals'

def check_illegal(user_input):
    for i in ILLEGAL_CHARACTERS:
        if i in user_input:
            print("Please enter a valid journal name.")
            return False
    return True
def check_blank(user_input):
    if " " in user_input:
        user_input = user_input.strip()
        if user_input == "":
            print("Please enter a valid journal name.")
            return False
    return True
def validate_input(user_input):
    if not check_blank(user_input):
        return False
    if not check_illegal(user_input):
        return False
    if " " in user_input:
        user_input = user_input.replace(" ", "_")
    return user_input

def check_journal(journal_name):
    journal_name = validate_input(journal_name)
    if not journal_name:
        return False
    full_path = os.path.join(BASE_PATH, journal_name)
    journal_path = os.path.exists(full_path)
    if not journal_path:
        return False
    return journal_name

def check_file_name_len(journal_name):
    if journal_name is None:
        return True
    if len(journal_name) > 100:
        print("Journal name too long")
        return False
    return True

def check_file_type():
    file_name = input("Enter entry name:\n ")
    if not file_name.endswith('.txt'):
        file_name = f"{file_name}.txt"
        file_name = validate_input(file_name)
    return file_name
if __name__ == "__main__":
    validate_input("!")