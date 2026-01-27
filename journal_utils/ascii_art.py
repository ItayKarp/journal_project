from datetime import datetime


def create_journal():
    print(r'''
       ___________________________
      /                           \
     |      CREATE NEW JOURNAL     |
      \___________________________/
          |                   |
          |   [ ]  [ ]  [ ]   |
          |___________________|

    "Every great story begins with
      a single blank page..."''')


def create_entry():
    # You can pass variables into f-strings like this:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(rf'''
     _______
    /      /   WRITE NEW ENTRY
   /      /    ---------------
  /______/   Created: {now}
 (______)      
  |    |       
  |    |       > Start typing below...
  |____|
    ''')


def remove_journal(journal_name):
    user_input = input(rf'''
      !!!!!!!!!!!!!!!!!!!!!!!!!
      !!   DANGER  ZONE      !!
      !!!!!!!!!!!!!!!!!!!!!!!!!
      !!   REMOVE JOURNAL    !!
      !!!!!!!!!!!!!!!!!!!!!!!!!

      Confirm Journal Name:
      
    ''')
    if journal_name == user_input:
        return True
    elif journal_name != user_input:
        print("Wrong journal name.")
        return False
    return False



def remove_entry(entry_name):
    user_input = input(r'''
     _____
    /     \  REMOVE ENTRY
   | () () | ------------
    \  ^  /
     |||||
            [ ! ] This action 
                cannot be undone.
    
    Enter the entry's name again:
    
    ''')
    if entry_name == user_input:
        return True
    elif entry_name != user_input:
        print("Wrong entry's name.")
        return False
    return True


def read_journal(journal_name):
    print(fr'''
    ________________   ________________
   /                \ /                \
  |  CHAPTER: ONE    |  "The sun rose   |
  |  --------------  |   over the...    |
  |  {journal_name}  |                  |
  |                  |   It was a day   |
  |                  |   to remember."  |
  |        -1-       |        -2-       |
   \________________/ \________________/
    ''')


def exit_app():
    # Note: Renamed from 'exit' to 'exit_app' to avoid
    # overriding Python's built-in exit() function.
    print(r'''
          __________________
         /                 /|
        /                 //
       /_________________//
      |        |         |/
      | JOURNAL| CLOSED  |
      |________|_________|

      "See you next time!"
    ''')


def init():
    print(r'''
          __________
       .-'          '-.
     /      WELCOME     \
    |    ____________    |
    |   |            |   |
    |   |            |   |
    |   |            |   |
    |___|            |___|
    |###|            |###|
      [ ACCESS GRANTED ]
      Initializing Pages...
    ''')


def line_break():
    # Note: Renamed 'break' to 'line_break' because
    # 'break' is a reserved keyword in Python loops.
    print('''
    ─── ❖ ─── ✦ ─── ❖ ─── ✦ ─── ❖ ─── ✦ ───
    ''')


def search():
    print(rf'''
Scanning: [====================>        ] 72%
    ''')
def art_create_entry(journal_name):
    current_time =datetime.now()
    print(rf"""
      _________________________
     |                         |           
     |   [ WRITE NEW ENTRY  ]  |          
     |Journal:{journal_name}   |           /|
     |time: {current_time}     |          / /
     |  Start typing below...  |         / /
     |   1. ________________   |      __/_/_
     |   2. ________________   |     |      |
     |   3. ________________   |     | [##] |
     |_________________________|     |______|

    """)