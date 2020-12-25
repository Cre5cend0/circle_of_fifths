"""Musical Keys"""
from core_files.chordProgression import Progression


class Key(Progression):
    """each musical note is a key. And, each key has it's own attributes such as its own set of chords, major/minor relativity
    Instantiate Key -> variable with Capital letter of the keySignature. eg: Instantiate C = Key('c') -> C major scale instantiated
    Instantiate Cm = Key('cm') -> C minor scale instantiated """

    def __init__(self, key_sign):
        Progression.__init__(self, key_sign)


C = Key('c')
D = Key('d')
E = Key('e')
F = Key('f')
G = Key('g')
A = Key('a')
B = Key('b')
Cm = Key('cm')
Dm = Key('dm')
Em = Key('em')
Fm = Key('fm')
Gm = Key('gm')
Am = Key('am')
Bm = Key('bm')
Dbm = Key('Dbm')
Ebm = Key('Ebm')
Gbm = Key('Gbm')
Abm = Key('Abm')
Bbm = Key('Bbm')
Db = Key('Db')
Eb = Key('Eb')
Gb = Key('Gb')
Ab = Key('Ab')
Bb = Key('Bb')
# Cb = Key('Cb')
# Cbm = Key('Cbm')
C_sharp = Key('c#')
D_sharp = Key('d#')
F_sharp = Key('f#')
G_sharp = Key('g#')
A_sharp = Key('a#')
# E_sharp = Key('e#')
# E_sharp_minor = Key('e#m') #todo
C_sharp_minor = Key('c#m')
D_sharp_minor = Key('d#m')
F_sharp_minor = Key('f#m')
G_sharp_minor = Key('g#m')
A_sharp_minor = Key('a#m')
