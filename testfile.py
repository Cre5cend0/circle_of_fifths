from core_files.fretboard import *
from core_files.musicalKeys import *
from core_files.musicalNotes import *
from core_files.scales import *
from core_files.chords import *

# Intervals test
# print(chrom_exec)
# print(halfStep('Eb'))
# print(wholeStep('Bb'))
# print(quadraStep('d'))
# print(wholeAndhalfStep('g'))
# print(wholeAndhalfStep_lower('f'))
# print(halfSteplower('Eb'))
# print(wholeSteplower('Bb'))

# Scales test
# Eb = Scale('Eb')
# print(Eb.get_notes())
# print(Eb.get_scale('dorian'))
# print(Eb.get_scale('phrygian'))
# print(Eb.get_scale('lydian'))
# print(Eb.get_scale('mixolydian'))
# print(Eb.get_scale('aeolian'))
# print(Eb.get_scale('locrian'))
# print(Eb.get_scale('pentatonic_minor'))
# print(Eb.get_scale('pentatonic_major'))

# print(Scale.scale_dict)

# Chords test
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
# print(B.harmony_dict)

# fretgen test
# my_list = Am.get_scale('minor')
# fretGen(my_list, show_note=False, tuning=['d', 'a', 'd', 'g', 'a', 'd'], capo=7)
#
# test = C.get_scale('minor')
# fretGen(test, show_note=True, capo=3)

# Triads test
G.maj_triads(show_note=False, is_chord=True)
# G.min_triads(show_note=False, is_chord=True)

# chord progression test
# scales = G.get_relativeScales()
# print(scales)
# try:
#     a = G.suggest_bar_chords_prog()
#     fretGen(next(a))
#     fretGen(next(a))
#     fretGen(next(a))
#     fretGen(next(a))
#     fretGen(next(a))
#     fretGen(next(a))
# except StopIteration:
#     pass
