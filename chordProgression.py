"""Randomly generate a few chords from the chosen key
to form a progression"""
import settings
from chords import *
from musicalKeys import *
from musicalNotes import circle_of_fifths_mj, circle_of_fifths_mi
from fretboard import fretGen

class Progression(Chord):
    def __init__(self, key_sign):
        Chord.__init__(self, key_sign)
        if self.mode == 'major':
            self.maj_chords = self.getRoot(), self.P4(), self.P5()
            self.min_chords = self.M2(), self.M3(), self.M6()
            self.dim_chord = self.M7()
        if self.mode == 'minor':
            self.min_chords = self.getRoot(), self.P4(), self.P5()
            self.maj_chords = self.m3(), self.m6(), self.m7()
            self.dim_chord = self.M2()

    def get_all_chords(self):
        return self.maj_chords, self.min_chords, self.dim_chord

    def maj_triads(self, **kwargs):
        my_chords = self.maj_chords
        progression = [full_chords_dict[(my_chords[i] + '_maj')] for i in range(len(my_chords))]
        for i in range(len(progression)):
            print((my_chords[i] + '_maj'), progression[i])
            print(fretGen(progression[i], **kwargs))
        # return progression[:]

    def min_triads(self, **kwargs):
        my_chords = self.min_chords
        progression = [full_chords_dict[(my_chords[i] + '_min')] for i in range(len(my_chords))]
        for i in range(len(progression)):
            print((my_chords[i] + '_min'), progression[i])
            print(fretGen(progression[i], **kwargs))

    def dim_triad(self, **kwargs):
        my_chords = self.dim_chord
        progression = [full_chords_dict[(my_chords[i] + '_dim')] for i in range(len(my_chords))]
        for i in range(len(progression)):
            print((my_chords[i] + '_dim'), progression[i])
            print(fretGen(progression[i], **kwargs))

    # def suggest_prog(self, starting_note=self.getRoot()):
    #     print('Nice!')
