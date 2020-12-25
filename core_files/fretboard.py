import settings
from core_files.musicalNotes import chrom_exec
from utilities.func_tools import flats_to_sharps

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

def fretGen(note_bunch, tuning=GuitarString.standard_tuning(), capo=0, show_note=False, is_chord=False):
    try:
        temp_bunch = []
        assert type(note_bunch[0]) is list
        for item in note_bunch:
            for i in item:
                temp_bunch.append(i)
        is_chord = True
    except AssertionError:
        temp_bunch = note_bunch[:]
    print(temp_bunch)
    if tuning == GuitarString.standard_tuning():
        pass
    else:
        tuning = GuitarString.custom_tuning(tuning)

    main_bunch = flats_to_sharps(temp_bunch)

    if not show_note:
        if capo != 0:
            print(f"Capo on fret {capo}")
        for string in tuning:
            fret = string.getstr_notes()
            final_fret = fret[capo:]
            fret_len = len(final_fret)

            if len(string.get_name()) > 1:
                print(string.get_name() + '|', end='')
            else:
                print(string.get_name() + ' |', end='')

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
            final_fret.append('\n')
            for i in final_fret:
                print(i, end="")
        print('\n')
    else:
        if capo != 0:
            print(f"Capo on fret {capo}")

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
        print('\n')

    if is_chord:
        pass
    # todo
    return

# for item in CHROMATICSCALE:
#     x = GuitarString(item)
#     string_dict[item] = x
#
# for item in accidentals.keys():
#     if item not in string_dict:
#         x = GuitarString(item)
#         string_dict[item] = x
