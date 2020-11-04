import settings
from musicalNotes import chrom_exec, accidentals, CHROMATICSCALE
from utilities import get_key

_flats_to_sharps = {'Db': 'c#', 'Eb': 'd#', 'Gb': 'f#', 'Ab': 'g#', 'Bb': 'a#', 'Cb': 'b', 'Fb': 'e'}

string_dict = {}


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
            if str_list[i] in string_dict:
                x = string_dict.get(str_list[i])
            else:
                x = GuitarString(str_list[i])
            my_set.append(x)
        return my_set[:]


_1_string = GuitarString('e')
_2_string = GuitarString('b')
_3_string = GuitarString('g')
_4_string = GuitarString('d')
_5_string = GuitarString('a')
_6_string = GuitarString('e')


def fretGen(note_bunch, tuning=GuitarString.standard_tuning(), capo=0, show_note=False):
    temp_bunch = note_bunch[:]
    if tuning == GuitarString.standard_tuning():
        pass
    else:
        tuning = GuitarString.custom_tuning(tuning)

    for i in range(len(temp_bunch)):
        if temp_bunch[i] in _flats_to_sharps.keys():
            temp_bunch.pop(i)
            temp_bunch.insert(i, _flats_to_sharps.get(note_bunch[i]))
            # print(temp_bunch)

    if not show_note:
        for string in tuning:
            fret = string.getstr_notes()
            print(string.get_name() + '|', end='')
            for note in fret:
                if note in temp_bunch:
                    i = fret.index(note)
                    fret.pop(i)
                    if i <= 12:
                        fret.insert(i, '--' + str(i) + '--')
                    elif 12 < i < 24:
                        fret.insert(i, '--' + str(i) + '-')

                else:
                    i = fret.index(note)
                    fret.pop(i)
                    if i == 0:
                        fret.insert(i, '--x--')
                    elif i <= 12:
                        fret.insert(i, '-----')
                    elif 12 < i < 24:
                        fret.insert(i, '---')
                    elif i >= 24:
                        fret.insert(i, '--')

            fret.append('\n')
            for i in fret:
                print(i, end="")
    else:
        for string in tuning:
            print(string.get_name() + '|', end='')
            fret = string.getstr_notes()
            for note in fret:
                if note in temp_bunch:
                    i = fret.index(note)
                    fret.pop(i)
                    if i <= 12:
                        fret.insert(i, '--' + note + '--')
                    elif 12 < i < 24:
                        fret.insert(i, '--' + note + '-')

                else:
                    i = fret.index(note)
                    fret.pop(i)
                    if i == 0:
                        fret.insert(i, '--x--')
                    elif i <= 12:
                        fret.insert(i, '-----')
                    elif 12 < i < 24:
                        fret.insert(i, '---')
                    elif i >= 24:
                        fret.insert(i, '--')

            fret.append('\n')
            for i in fret:
                print(i, end="")
    return


for item in CHROMATICSCALE:
    x = GuitarString(item)
    string_dict[item] = x

for item in accidentals.keys():
    if item not in string_dict:
        x = GuitarString(item)
        string_dict[item] = x

