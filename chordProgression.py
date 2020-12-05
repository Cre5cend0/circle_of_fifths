"""Randomly generate a few chords from the chosen key
to form a progression"""
import settings
from chords import *


class Progression(Chord):
    def __init__(self, key_sign):
        Chord.__init__(self, key_sign)

    def one_four_five(self):
        if self.mode == 'major':
            scale = self.get_scale(self.mode)
            progression = [full_chords_dict[scale[0] + '_maj'], full_chords_dict[scale[3] + '_maj'],
                           full_chords_dict[scale[4] + '_maj']]
            return progression[:]

