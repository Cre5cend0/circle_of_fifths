import time

import settings
from core_files import chords
from core_files.musicalNotes import chrom_exec
from utilities import rangen
from utilities.func_tools import flats_to_sharps, get_key

_flats_to_sharps = {'Db': 'c#', 'Eb': 'd#', 'Gb': 'f#', 'Ab': 'g#', 'Bb': 'a#', 'Cb': 'b', 'Fb': 'e'}


class GuitarString:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def getstr_notes(self):
        """ Get all the notes which belong to that guitar string """
        note_set = []
        index = chrom_exec.index(self.name)
        for i in range(settings.my_neck + 1):
            note_set.append(chrom_exec[index + i])

        return note_set[:]

    @classmethod
    def standard_tuning(cls):
        """returns guitar string objects in standard tuning format"""
        tuning = (_1_string, _2_string, _3_string, _4_string, _5_string, _6_string)
        return tuning

    @classmethod
    def custom_tuning(cls, str_list):
        """ Takes one argument, str_list -> list of individual guitar string names
        returns guitar string objects as tuned by the player"""
        my_set = []
        for i in range(6):
            x = GuitarString(str_list[i])
            my_set.append(x)
        return my_set[:]


# Default guitar string objects
_1_string = GuitarString('e')
_2_string = GuitarString('b')
_3_string = GuitarString('g')
_4_string = GuitarString('d')
_5_string = GuitarString('a')
_6_string = GuitarString('e')


# get the notes of first 3 or 4 or middle 3 strings, etc. todo

def fretGen(note_bunch, tuning=GuitarString.standard_tuning(), capo=0, show_note=False, is_chord=False, string_range=6,
            fret_range=settings.my_key):
    """
    Prints fret board to the console. Set desired features using parameters:
    note_bunch -> list of notes appearing on fretboard. Can contain lists within this list where each element represents a chord,
    tuning -> Takes a list of notes as string names,
    capo -> Sets up a virtual Capo on the fretboard,
    show_note -> Set to True to see the note names on the fret board and False to see the fret numbers,
    is_chord -> Set to True if the input is a chord type. Can remain in default if passing a bunch of chords as argument,
    string_range -> select the strings you want to view by passing the lowest string's number,
    fret_range -> Set the range of frets you want to view the notes in. i.e, Fret boxes
    """

    # Setting some default variables
    num1, num2 = 0, settings.my_key
    chord_set = None

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # mounting the strings on guitar as tuned by player
    if tuning == GuitarString.standard_tuning():
        pass
    else:
        tuning = GuitarString.custom_tuning(tuning)

    # If using a capo, printing the position on capo on fretboard in bold
    if capo != 0:
        print()
        print('#' * 40)
        print(f"Capo on fret {capo}".upper())
        print('#' * 40)
        print()

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def chord_sequencer():
        """ If notes to be printed is a set of chords, sending  one chord item after the other """
        for item in note_bunch:
            yield item

    # Checking if the list to be printed is a set of chords or not
    try:
        temp_bunch = []
        assert type(note_bunch[0]) is list
        chord_set = chord_sequencer()  # if first note in note bunch is a list of notes, then starting chord sequencer
        count = len(note_bunch)
        ch = next(chord_set)
        for i in ch:
            temp_bunch.append(i)
        is_chord = True
    except AssertionError:
        # Setting the default values to temporary bunch of notes to be printed
        temp_bunch = note_bunch[:]
        count = 1

    if is_chord:
        # generating fret boxes/shapes to display
        num1, num2 = rangen.fret_range(capo)
    else:
        # displaying all notes being to be printed
        print(temp_bunch)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    while count > 0:  # starting a loop to print each chord one after the other, or whole set of notes once.
        main_bunch = temp_bunch[:]

        # printing chord name and notes
        if is_chord:
            name = get_key(chords.Chord.get_harmony_dict(), temp_bunch)
            print(f'{name}: {temp_bunch}')

        for string in tuning:
            fret = string.getstr_notes()  # getting all notes of a guitar string
            final_fret = fret[capo:]  # truncating the notes on a guitar string wrt capo

            # printing string names before each guitar string
            if len(string.get_name()) > 1:
                print(string.get_name() + '|', end='')
            else:
                print(string.get_name() + ' |', end='')

            # printing capo placeholder
            if capo != 0:
                print(f'\u2561{capo}\u255e', end='')

            # replacing each note on the string with fret position
            for index in range(len(final_fret)):
                note = final_fret[index]  # extracting fret note

                if index <= 9:
                    # giving wider space between frets less than or equal to 9
                    if note in main_bunch:
                        final_fret.pop(index)
                        if not show_note:
                            final_fret.insert(index, '--' + str(index) + '--') # printing fret number with fret distances
                        else:
                            if len(note) > 1:
                                final_fret.insert(index, '--' + str(note) + '-')  # printing musical note with fret distances
                            else:
                                final_fret.insert(index, '--' + str(note) + '--')
                    else:
                        final_fret.pop(index)
                        if index == 0:
                            final_fret.insert(index, '--x--')
                        else:
                            final_fret.insert(index, '-----')
                else:
                    # giving narrow space between frets greater than 9
                    if note in main_bunch:
                        final_fret.pop(index)
                        if not show_note:
                            final_fret.insert(index, '-' + str(index) + '-') # printing fret number with fret distances
                        else:
                            if len(note) > 1:
                                final_fret.insert(index, '-' + str(note) + '-')  # printing musical note with fret distances
                            else:
                                final_fret.insert(index, '-' + str(note) + '--')
                    else:
                        final_fret.pop(index)
                        final_fret.insert(index, '----')

            # setting the last fret positions to be printed wrt capo and/or is_chord
            if is_chord:
                ult_fret = final_fret[num1:num2]
            else:
                ult_fret = final_fret[:]

            ult_fret.append('\n') # adding a new line at the end of each string

            for i in ult_fret:
                print(i, end="") # printing each note in guitar string as required

        # If input notes were a set of chords, prints each chord one after the other
        if count > 1:
            main_bunch.clear()
            temp_bunch.clear()
            ch = next(chord_set) # invoking the next set of chords
            for i in ch:
                temp_bunch.append(i)

        count -= 1  # closing the loop by decrementing count
        time.sleep(2)  # giving a pause between each chord being printed
    return ""

# for item in CHROMATICSCALE:
#     x = GuitarString(item)
#     string_dict[item] = x
#
# for item in accidentals.keys():
#     if item not in string_dict:
#         x = GuitarString(item)
#         string_dict[item] = x
