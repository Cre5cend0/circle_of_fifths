from circle_of_fifths import settings
from circle_of_fifths import fretGen
from circle_of_fifths import Key
from circle_of_fifths import pref_finder
from circle_of_fifths.core_files.scales import Scale

settings.my_key = Key('a')
pref_finder()



# print(E.get_chord_names)
# print(E.get_chord_names[0])
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

# print(B.harmony_dict)

# fretgen test
# my_list = Gm.get_scale('minor')
# fretGen(my_list, show_note=False)
#
# test = C.get_scale('minor')
# fretGen(test, show_note=True, capo=3)

# Triads test

# Dm.maj_triads(show_note=False, is_chord=False)
# Dm.min_triads(show_note=False, is_chord=False)
# Dm.dim_triad(show_note=False, is_chord=False) #todo

A = Scale('A')
a = A.get_scale('major')
# b = A.chordGen('major')
fretGen(a, is_chord=True, show_note=False, capo=5)


# chord progression test
# scales = Eb.get_relativeScales()
# print(scales)

# a = G.suggest_bar_chords_prog('a')
# fretGen(a)


