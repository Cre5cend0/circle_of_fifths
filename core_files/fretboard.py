import time

import settings
from core_files import chords
from core_files.musicalNotes import chrom_exec
from utilities.func_tools import flats_to_sharps, get_key

_flats_to_sharps = {'Db': 'c#', 'Eb': 'd#', 'Gb': 'f#', 'Ab': 'g#', 'Bb': 'a#', 'Cb': 'b', 'Fb': 'e'}


class GuitarString:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def getstr_notes(self):
        note_set = []
        index = chrom_exec.index(self.name)
        for i in range(settings.my_neck + 1):
            note_set.append(chrom_exec[index + i])

        return note_set[:]

    @classmethod
    def standard_tuning(cls):
        tuning = (_1_string, _2_string, _3_string, _4_string, _5_string, _6_string)
        return tuning

    @classmethod
    def custom_tuning(cls, str_list):
        my_set = []
        for i in range(6):
            x = GuitarString(str_list[i])
            my_set.append(x)
        return my_set[:]


_1_string = GuitarString('e')
_2_string = GuitarString('b')
_3_string = GuitarString('g')
_4_string = GuitarString('d')
_5_string = GuitarString('a')
_6_string = GuitarString('e')


# get the notes of first 3 or 4 or middle 3 strings, etc. todo
# show notes in bunches of 3 or 4 frets like actual chord shapes todo

def fretGen(note_bunch, tuning=GuitarString.standard_tuning(), capo=0, show_note=False, is_chord=False, string_range=6,
            fret_range=settings.my_key):
    """
    Prints fret board to the console. Set desired features using parameters:
    note_bunch -> list of notes appearing on fretboard. Can contain lists within this list where each element represents a chord,
    tuning -> Takes a list of notes as string names,
    capo -> Sets up a virtual Capo on the fretboard,
    show_note -> Set to True to see the note names on the fret board and False to see the fret numbers,
    is_chord -> Set to True if the input is a chord type,
    string_range -> select the strings you want to view by passing the lowest string's number,
    fret_range -> Set the range of frets you want to view the notes in. i.e, Fret boxes
    """
    chord_set = None
    if tuning == GuitarString.standard_tuning():
        pass
    else:
        tuning = GuitarString.custom_tuning(tuning)

    if capo != 0:
        print()
        print('#' * 40)
        print(f"Capo on fret {capo}".upper())
        print('#' * 40)
        print()

    def chord_seq():
        for item in note_bunch:
            yield item

    try:
        temp_bunch = []
        assert type(note_bunch[0]) is list
        chord_set = chord_seq()
        count = len(note_bunch)
        ch = next(chord_set)
        for i in ch:
            temp_bunch.append(i)
        is_chord = True
    except AssertionError:
        temp_bunch = note_bunch[:]
        count = 1

    if not is_chord:
        print(temp_bunch)

    while count > 0:
        main_bunch = temp_bunch[:]
        if is_chord:
            name = get_key(chords.Chord.get_harmony_dict(), temp_bunch)
            print(f'{name}: {temp_bunch}')
        if not show_note:

            for string in tuning:

                fret = string.getstr_notes()
                final_fret = fret[capo:]

                if len(string.get_name()) > 1:
                    print(string.get_name() + '|', end='')
                else:
                    print(string.get_name() + ' |', end='')

                if capo != 0:
                    print(f'\u2561{capo}\u255e', end='')

                for index in range(len(final_fret)):
                    note = final_fret[index]
                    if index <= 9:
                        if note in main_bunch:
                            final_fret.pop(index)
                            final_fret.insert(index, '--' + str(index) + '--')
                        else:
                            final_fret.pop(index)
                            if index == 0:
                                final_fret.insert(index, '--x--')
                            else:
                                final_fret.insert(index, '-----')
                    else:
                        if note in main_bunch:
                            final_fret.pop(index)
                            final_fret.insert(index, '-' + str(index) + '-')
                        else:
                            final_fret.pop(index)
                            final_fret.insert(index, '----')

                if is_chord:  # add to show_notes=False todo
                    final_fret = final_fret[:5]
                final_fret.append('\n')

                for i in final_fret:
                    print(i, end="")

        else:
            for string in tuning:
                fret = string.getstr_notes()
                final_fret = fret[capo:]
                fret_len = len(final_fret)
                if len(string.get_name()) > 1:
                    print(string.get_name() + '|', end='')
                else:
                    print(string.get_name() + ' |', end='')
                for index in range(fret_len):
                    note = final_fret[index]
                    if index <= 9:
                        if note in main_bunch:
                            final_fret.pop(index)
                            if len(note) > 1:
                                final_fret.insert(index, '--' + str(note) + '-')
                            else:
                                final_fret.insert(index, '--' + str(note) + '--')
                        else:
                            final_fret.pop(index)
                            if index == 0:
                                final_fret.insert(index, '--x--')
                            else:
                                final_fret.insert(index, '-----')
                    else:
                        if note in main_bunch:
                            final_fret.pop(index)
                            if len(note) > 1:
                                final_fret.insert(index, '-' + str(note) + '-')
                            else:
                                final_fret.insert(index, '-' + str(note) + '--')
                        else:
                            final_fret.pop(index)
                            final_fret.insert(index, '----')

                final_fret.append('\n')
                for i in final_fret:
                    print(i, end="")

        if count > 1:
            main_bunch.clear()
            temp_bunch.clear()
            ch = next(chord_set)
            for i in ch:
                temp_bunch.append(i)
        count -= 1
        time.sleep(2)
    return ""

# for item in CHROMATICSCALE:
#     x = GuitarString(item)
#     string_dict[item] = x
#
# for item in accidentals.keys():
#     if item not in string_dict:
#         x = GuitarString(item)
#         string_dict[item] = x
