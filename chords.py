"""Generates chords by stacking notes"""
from intervals import *
from scales import Scale
from utilities import applyAll, runMethod


class Chord(Scale):
    _chord_dict = {
        'maj'     : [unison, M3, P5],
        'min'     : [unison, m3, P5],
        'dom7'    : [unison, M3, P5, m7],
        '7'       : [unison, M3, P5, m7],
        'min7'    : [unison, m3, P5, m7],
        'maj7'    : [unison, M3, P5, M7],
        'sus4'    : [unison, P4, P5],
        'sus2'    : [unison, M2, P5],
        '7sus4'   : [unison, P4, P5, m7],
        '7sus2'   : [unison, M2, P5, m7],
        '6'       : [unison, M3, P5, M6],
        'min6'    : [unison, m3, P5, M6],
        'dim'     : [unison, m3, b5],
        'dim7'    : [unison, m3, b5, M6],
        'aug'     : [unison, M3, m6],
        '7b5'     : [unison, M3, b5, m7],
        '7#5'     : [unison, M3, m6, m7],
        'min7b5'  : [unison, m3, b5, m7],
        'half_dim': [unison, m3, b5, m7],
        'minmaj7' : [unison, m3, P5, M7],
        'maj7#5'  : [unison, M3, m6, M7],
        'maj7b5'  : [unison, M3, b5, M7],
        '9'       : [unison, M3, P5, m7, M2],
        'min9'    : [unison, m3, P5, m7, M2],
        'maj9'    : [unison, M3, P5, M7, M2],
        '7#9'     : [unison, M3, P5, m7, m3],
        '7b9'     : [unison, M3, P5, m7, m2],
        '7#9b5'   : [unison, M3, b5, m7, m3],
        '6/9'     : [unison, M3, P5, M6, M2],
        # in 6/9 chords, due to practical circumstances, however, the fifth is often omitted and/or the chord is
        # played inverted.
        '9#5'     : [unison, M3, m6, m7, M2],
        '9b5'     : [unison, M3, b5, m7, M2],
        'min9b5'  : [unison, m3, b5, m7, M2],
        '11'      : [unison, M3, P5, m7, M2, P4],
        'min11'   : [unison, m3, P5, m7, M2, P4],
        '11b9'    : [unison, M3, P5, m7, m2, P4],
        '13'      : [unison, M3, P5, m7, M2, P4, M6],
        'min13'   : [unison, m3, P5, m7, M2, P4, M6],
        'maj13'   : [unison, M3, P5, M7, M2, P4, M6],
        'maj13#11': [unison, M3, P5, M7, M2, tritone, M6],
        'add9'    : [unison, M3, P5, M2],
        'madd9'   : [unison, m3, P5, M2],
        '5'       : [unison, P5],
        'b5'      : [unison, M3, b5],
        '#5'      : [unison, M3, m6],
        'maj11'   : [unison, M3, P5, M7, M2, P4],
        'min6/9'  : [unison, m3, P5, M6, M2],
        'minmaj9' : [unison, m3, P5, M7, M2],
        'min7#5'  : [unison, m3, m6, m7],
        '7/6'     : [unison, M3, P5, M6, m7],
        '7b5b9'   : [unison, M3, b5, m7, m2],
        '7#5b9'   : [unison, M3, m6, m7, m2],
        '7b5#9'   : [unison, M3, b5, m7, m3],
        '7#5#9'   : [unison, M3, m6, m7, m3],
        '7#11'    : [unison, M3, P5, m7, M2, tritone],
        '7b9#11'  : [unison, M3, P5, m7, m2, tritone],
        '13b9'    : [unison, M3, P5, m7, m2, P4, M6],
        '13b5b9'  : [unison, M3, b5, m7, m2, P4, M6],
        '13#11'   : [unison, M3, P5, m7, M2, tritone, M6],
        '13b9#11' : [unison, M3, P5, m7, m2, tritone, M6]
    }

    harmony_dict = {}

    def __init__(self, key_sign):
        Scale.__init__(self, key_sign)
        self.name = None

    def chordGen(self, param):
        scale_step = self._chord_dict[param]
        self.name = param
        if (self.root + '_' + self.name) not in self.harmony_dict:
            chord_notes = runMethod(self, scale_step)
            self.harmony_dict.update({(self.root + '_' + self.name): chord_notes})
        else:
            return self.harmony_dict.get((self.root + '_' + self.name))
        return chord_notes

    @classmethod
    def get_harmony_dict(cls):
        return cls.harmony_dict

    @classmethod
    def chord_list(cls):
        li = cls._chord_dict.keys()
        return li


y = Chord.chord_list()
for item in CHROMATICSCALE:
    x = Chord(item)
    applyAll(x.chordGen, y)

