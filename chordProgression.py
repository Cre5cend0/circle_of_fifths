"""Randomly generate a few chords from the chosen key
to form a progression"""
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

    def suggest_bar_chords_prog(self, next_chord):
        all_chords = self.get_all_chords()
        major_chords = all_chords[0]
        minor_chords = all_chords[1]
        dim_chord = all_chords[2]
        if self.mode == 'major':
            one_chord, four_chord, five_chord = all_chords[0]
            two_chord, three_chord, six_chord = all_chords[1]
            seven_chord = all_chords[2]  # todo
            chord_order = (one_chord, two_chord, three_chord, four_chord, five_chord, six_chord, seven_chord)
        else:
            three_chord, six_chord, seven_chord = all_chords[0]
            one_chord, four_chord, five_chord = all_chords[1]
            two_chord = all_chords[2]  # todo
            chord_order = (one_chord, two_chord, three_chord, four_chord, five_chord, six_chord, seven_chord)
        print(chord_order)
        i = None
        li = []
        if self.mode == 'major':
            li.append(all_my_chords[chord_order[0] + '_maj'])
        else:
            li.append(all_my_chords[chord_order[0] + '_min'])
        if next_chord in chord_order:
            i = chord_order.index(next_chord)
            if next_chord in major_chords:
                li.append(all_my_chords[chord_order[i] + '_maj'])
            elif next_chord in minor_chords:
                li.append(all_my_chords[chord_order[i] + '_min'])
            else:
                li.append(all_my_chords[chord_order[i] + '_dim'])

        if i == 2:
            li.append(all_my_chords[chord_order[4] + '_maj7'])

        for item in li:
            yield item
