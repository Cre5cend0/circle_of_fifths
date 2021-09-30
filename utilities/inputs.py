import os
import sys
import settings
from core_files.chords import Chord
from core_files.fretboard import fretGen

expected_inputs = [
    # list of generally accepted inputs. Does not include
    # inputs such as 'try key' or 'go to', 'show', 'change tuning'
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
    type 'show' followed by another keyword like intervals, scales, chord list, chord, fretboard etc to view them
    type 'my turn' to switch control on user input. You can start asking questions
"""


def inputChecker(user_input):
    new_key = None
    if user_input in expected_inputs:
        if user_input == 'exit' or user_input == 'quit':
            sys.exit()
        elif user_input == 'yes' or user_input == 'y' or user_input == 'Yes' or user_input == '':
            return 1
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
        try:
            new_key = Key(user_input[8:])
            settings.my_key = new_key
            print('Changing key to ' + user_input[8:])
            # if settings.user_turn:
            #     return input('>> ')
            # return 0
        except KeyError:
            return ValueError

    elif user_input[:4] == 'show':
        value = user_input[5:]
        if value == 'chord list':
            print(Chord.get_chord_list())
            return
        elif value[:5] == 'chord':
            print(fretGen(settings.my_key.chordGen(value[6:]), is_chord=True, show_note=False, capo=settings.capo))
            return
        else:
            raise ValueError

    else:
        return ValueError

