from .menus import clear_screen
from . import menus
def handle_user_input(user_input):
    while True:
        if user_input == "1":
            journal_name = menus.create_journal_menu()
            if not journal_name:
                print("Journal name already exists.")
                return
            if journal_name:
                return
            user_create_entry = input("Would you like to create an entry? type 'y' for yes , 'n' for no\n").lower()
            if user_create_entry == "y":
                menus.create_entry_menu(journal_name)
            return
        elif user_input == "2":
            menus.create_entry_menu()
            return
        elif user_input == "3":
            menus.read_journal_menu()
            return
        elif user_input == "4":
            menus.remove_journal_menu()
            return
        elif user_input == "5":
            menus.remove_entry_menu()
            return
        elif user_input == "6":
            menus.exit_menu()
        else:
            clear_screen()
            print("Please enter a valid input. 1, 2 or 3....")
            return

def main_menu():
    while True:
        menus.instructions_menu()
        user_input = input("")
        handle_user_input(user_input)

if __name__ == "__main__":
    main_menu()