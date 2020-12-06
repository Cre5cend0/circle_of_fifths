from musicalNotes import *
import settings
from fretboard import *
from musicalKeys import *

# print(chrom_exec)
# print(halfStep('Eb'))
# print(wholeStep('Bb'))
# print(quadraStep('d'))
# print(wholeAndhalfStep('g'))
# print(wholeAndhalfStep_lower('f'))
# print(halfSteplower('Eb'))
# print(wholeSteplower('Bb'))
#
#
#
# Eb = Scale('Eb')
# print(Eb.getNotes())
# print(Eb.get_scale('dorian'))
# print(Eb.get_scale('phrygian'))
# print(Eb.get_scale('lydian'))
# print(Eb.get_scale('mixolydian'))
# print(Eb.get_scale('aeolian'))
# print(Eb.get_scale('locrian'))
# print(Eb.get_scale('pentatonic_minor'))
# print(Eb.get_scale('pentatonic_major'))
#
# print(Scale.scale_dict)
#
# B = Chord('b')
# print(B.chordGen('maj'))
# print(B.chordGen('min'))
# print(B.chordGen('sus2'))
# print(B.chordGen('sus4'))
# print(B.chordGen('min7'))
# print(B.chordGen('dim'))
# print(B.chordGen('aug'))
# print(B.chordGen('maj7b5'))
# print(B.chordGen('min7b5'))
# print(B.chordGen('13b9#11'))
#
# Em = Chord('c')
# print(Em.chordGen('maj'))
# print(Em.chordGen('min'))
# print(Em.chordGen('sus2'))
# print(Em.chordGen('sus4'))
# print(Em.chordGen('min7'))
# print(Em.chordGen('dim'))
# print(Em.chordGen('aug'))
# print(Em.chordGen('maj7b5'))
# print(Em.chordGen('min7b5'))
# print(Em.chordGen('13b9#11'))
# print(Em.chordGen('maj13#11'))
# print(Em.chordGen('minmaj9'))
# print(Em.chordGen('11b9'))

# print(B.harmony_dict)
#
# search = B.chordGen('maj')
# print(search)
# print(fretGen(search, show_note=False))
#
# my_list = Am.get_scale('aeolian')
# print(my_list)
# print(fretGen(my_list, show_note=False, capo=7))
E.maj_triads(show_note=False, capo=4)
E.min_triads(show_note=False, capo=4)
scale = E.get_scale('major')
fretGen(scale)
