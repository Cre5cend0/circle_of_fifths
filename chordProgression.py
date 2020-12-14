"""Randomly generate a few chords from the chosen key
to form a progression"""
from random import randrange, choice

import settings
from chords import *
from musicalNotes import circle_of_fifths_mj, circle_of_fifths_mi
from fretboard import fretGen

all_my_chords = Chord.get_harmony_dict()


class Progression(Chord):
    def __init__(self, key_sign):
        Chord.__init__(self, key_sign)
        if self.mode == 'major':
            self.maj_chords = self.getRoot(), self.P4(), self.P5()
            self.min_chords = self.M2(), self.M3(), self.M6()
            self.dim_chord = self.M7()
        if self.mode == 'minor':
            self.maj_chords = self.m3(), self.m6(), self.m7()
            self.min_chords = self.getRoot(), self.P4(), self.P5()
            self.dim_chord = self.M2()

    def get_all_chords(self):
        return self.maj_chords, self.min_chords, self.dim_chord

    def maj_triads(self, **kwargs):
        my_chords = self.maj_chords
        progression = [all_my_chords[(my_chords[i] + '_maj')] for i in range(len(my_chords))]
        for i in range(len(progression)):
            print((my_chords[i] + '_maj'), progression[i])
            print(fretGen(progression[i], **kwargs))

    def min_triads(self, **kwargs):
        my_chords = self.min_chords
        progression = [all_my_chords[(my_chords[i] + '_min')] for i in range(len(my_chords))]
        for i in range(len(progression)):
            print((my_chords[i] + '_min'), progression[i])
            print(fretGen(progression[i], **kwargs))

    def dim_triad(self, **kwargs):
        my_chords = self.dim_chord
        progression = [all_my_chords[(my_chords[i] + '_dim')] for i in range(len(my_chords))]
        for i in range(len(progression)):
            print((my_chords[i] + '_dim'), progression[i])
            print(fretGen(progression[i], **kwargs))

    def suggest_bar_chords_prog(self, next_chord=None):
        all_chords = self.get_all_chords()
        major_chords = all_chords[0]
        minor_chords = all_chords[1]
        dim_chord = all_chords[2]

        if self.mode == 'major':
            one_chord, four_chord, five_chord = major_chords
            two_chord, three_chord, six_chord = minor_chords
            seven_chord = dim_chord
            ch_order = (one_chord, two_chord, three_chord, four_chord, five_chord, six_chord, seven_chord)
        else:
            three_chord, six_chord, seven_chord = major_chords
            one_chord, four_chord, five_chord = minor_chords
            two_chord = dim_chord
            ch_order = (one_chord, two_chord, three_chord, four_chord, five_chord, six_chord, seven_chord)
        print(ch_order)

        i = None
        ch_list = []

        if self.mode == 'major':
            ch_list.append(all_my_chords[one_chord + '_maj'])
        else:
            ch_list.append(all_my_chords[one_chord + '_min'])

        if next_chord in ch_order:
            i = ch_order.index(next_chord)
            if i == 0:
                i = randrange(1, 6)
            if next_chord in major_chords:
                ch_list.append(all_my_chords[ch_order[i] + '_maj'])
            elif next_chord in minor_chords:
                ch_list.append(all_my_chords[ch_order[i] + '_min'])
            else:
                ch_list.append(all_my_chords[ch_order[i] + '_dim7'])
        else:
            i = 2
            if self.mode == 'major':
                ch_list.append(all_my_chords[three_chord + '_min'])
            else:
                ch_list.append(all_my_chords[three_chord + '_maj'])

        while ch_list[0] != ch_list[-1]:

            if i == 1:
                if self.mode == 'major':
                    ch_list.append(all_my_chords[five_chord + '_maj7'])
                    i = 4
                else:
                    ch_list.append(all_my_chords[one_chord + '_min'])

            if i == 2:
                if self.mode == 'major':
                    ch_list.append(all_my_chords[six_chord + '_min'])
                else:
                    ch_list.append(all_my_chords[six_chord + '_maj'])
                i = 5

            if i == 3:
                i = choice([0, 4])
                if self.mode == 'major':
                    if i == 0:
                        ch_list.append(all_my_chords[one_chord + '_maj'])
                        break
                    elif i == 4:
                        ch_list.append(all_my_chords[five_chord + '_dom7'])
                else:
                    ch_list.append(all_my_chords[ch_order[i] + '_min'])

            if i == 4:
                if self.mode == 'major':
                    ch_list.append(all_my_chords[one_chord + '_maj'])
                else:
                    ch_list.append(all_my_chords[one_chord + '_min'])
                break

            if i == 5:
                if self.mode == 'major':
                    ch_list.append(all_my_chords[two_chord + '_min'])
                else:
                    ch_list.append(all_my_chords[two_chord + '_dim7'])
                i = 1

            if i == 6:
                i = 4

        for chord in ch_list:
            yield chord
