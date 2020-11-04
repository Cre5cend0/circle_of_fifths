"""Musical Keys"""
from chords import Chord


class Key(Chord):
    """each musical note is a key. And, each key has it's own attributes such as its own set of chords, major/minor relativity
    Instantiate Key -> variable with Capital letter of the keySignature. eg: Instantiate C = Key('c') -> C major scale instantiated
    Instantiate Cm = Key('cm') -> C minor scale instantiated """

    def __init__(self, key_sign):
        Chord.__init__(self, key_sign)
        self.relativeMinor = self.getNotes()[5]
        self.relativeMajor = self.getNotes()[2]

    def getRoot(self):
        return self.root

    def getRelativemajor(self):
        return self.relativeMajor.title()

    def getRelativeminor(self):
        return self.relativeMinor.title() + 'm'

    def getNotes(self):
        '''return a list of all the notes in the Key Signature'''
        return self.scale(self.mood)

    def scale(self, param):
        '''Returns all the valid notes in the Key Signature'''
        scale_step = self.modes[param]
        mode = kd.get_key(self.modes, scale_step)
        if self.key not in Chord.keyDict:
            mode = kd.get_key(self.modes, scale_step)
            my_notes = utilities.apply.applyEach(scale_step, self.root)
            my_notes.insert(0, self.root)
            first_char = []
            try:

                for i in range(len(my_notes) - 1):
                    if my_notes[i][0] in semantics.keys():
                        check_note = semantics[my_notes[i][0]]
                    else:
                        check_note = my_notes[i][0]

                    if check_note not in first_char:
                        first_char.append(check_note)
                    else:
                        new_note = nC.convert(my_notes[i])
                        my_notes[i] = new_note
                        if my_notes[i][0] in semantics.keys():
                            check_note = semantics[my_notes[i][0]]
                            first_char.append(check_note)

            except IndexError:
                pass

            finally:
                my_notes.pop()
                first_char.clear()
                Chord.keyDict.update({self.key: my_notes})
        else:
            return Chord.keyDict.get(self.key)

        return my_notes

    @classmethod
    def convert(cls, li):
        '''Takes one argument, returns a flat version for a sharp note or vice versa for item in iterable'''
        new_list = list(map(nC.convert, li))
        return new_list


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
Cb = Key('Cb')
Cbm = Key('Cbm')
C_sharp = Key('c#')
D_sharp = Key('d#')
F_sharp = Key('f#')
G_sharp = Key('g#')
A_sharp = Key('a#')
E_sharp = Key('e#')
E_sharp_minor = Key('e#m')
C_sharp_minor = Key('c#m')
D_sharp_minor = Key('d#m')
F_sharp_minor = Key('f#m')
G_sharp_minor = Key('g#m')
A_sharp_minor = Key('a#m')
