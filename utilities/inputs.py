import os
import sys
import settings
from core_files.chords import Chord

expected_inputs = [
    # list of generally accepted inputs. Does not include
    # inputs such as 'try key' or 'go to', 'show', change tuning
    # as they are followed by another argument.

    'yes', 'Yes', 'No', 'n', 'y', 'no', 'help',
    'exit', 'quit', '', 'restart', 'fav', 'my turn', 'resume'
]

# clone = Chord.harmony_dict.copy()
# items = clone.keys()
# for i in items:
#     # attaching all the key names to expected_inputs
#     expected_inputs.append(i)

help = """
    type 'y', 'yes', 'Yes' or press enter to Proceed;
    type 'n', 'no' or 'No' to deny;
    type 'exit' or 'quit' to exit program;
    type 'try key' followed by a space and key to change key;
    type 'go to' followed by space and topic name to jump to any topic;
    type 'restart' to restart program;
    type 'go to' followed by a topic to navigate through questions
    type 'fav' to add something to favourites
    type 'show' followed by anything like Intervals, scales,, fretboard etc to view them
    type 'my turn' to switch control on user input. You can start asking questions
"""


def inputChecker(user_input):
    new_key = None
    if user_input in expected_inputs:
        if user_input == 'exit' or user_input == 'quit':
            sys.exit()
        elif user_input == 'yes' or user_input == 'y' or user_input == 'Yes' or user_input == '':
            return 10
        elif user_input == 'no' or user_input == 'n' or user_input == 'No':
            return 2
        elif user_input == 'restart':
            ask = input('Are you sure? ')
            inputChecker(ask)
            if ask == 'yes' or ask == 'y' or ask == 'Yes' or ask == '':
                os.execl(sys.executable, sys.executable, *sys.argv)

        elif user_input == 'help':
            print(help)
            return

        elif user_input == 'my turn':
            return input('How can I help? ')

        elif user_input == 'resume':
            # switching role from user to app to ask questions
            return 7

    elif user_input[0:7] == 'try key':
        from core_files.musicalKeys import Key
        from utilities.interact import user_turn
        try:
            new_key = Key(user_input[8:])
            settings.my_key = new_key
            print()
            print('Changing key to ' + user_input[8:])
            if user_turn:
                return input('>> ')
            return 5
        except KeyError:
            return ValueError
    else:
        return ValueError

