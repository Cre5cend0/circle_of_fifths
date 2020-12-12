from intervals import Interval
from musicalNotes import CHROMATICSCALE, wholeStep, halfStep, wholeAndhalfStep, quadraStep, semantics
from utilities import applyEach, get_key, convert, flats_to_sharps


class Scale(Interval):
    """

    The easiest way to explain scales is as a collection of notes that because of a musical reason
    have been grouped together. The benefit of knowing scales in music is that you know how to orient
    yourself among notes. This will among other things give you a foundation for improvising – notes in
    a particular scale always sound good played together – and composing.

    The modes can become useful when you are playing a scale over a chord in an
    improvisation situation. Some modes (Ionian, Lydian and Mixolydian) will sound
    good with Major or Dominant chords and some (Dorian, Phrygian, Aeolian and Locrian)
    will sound good with Minor chords. Exceptions from this is possible, although.

    If we take the C Major Scale and play it in the Dorian Mode, what happens is that
    the notes remain the same, but the starting point is altered.
    In other words, C - D - E - F - G - A - B change to D - E - F - G - A - B - C and become Dorian.

    The Melodic Minor Scale differs from the Natural Minor Scale by the sixth and seventh notes,
    which are raised a semi-step. This scale is also some kind of peculiar since it is sometimes played
    differently ascending and descending. A melodic minor scale played the same both ascending
    and descending is the Jazz minor scale.

    Improvising with the Pentatonic Scale:
    The Pentatonic Scale is a flexible scale for improvising and apart from the standard way,
    which is combining a scale with chords in the same key, you could also be outside the key.
    By “being outside the key” means that you don't necessarily play chords and scale that belongs
    to the same key. For example, you could play G Major Pentatonic over a C Major chord or
    E Minor Pentatonic over an A Minor chord, this is called superimposing.

    The Enigmatic Scale was invented by the Italian composer Giuseppe Verdi.
    It is a somewhat obscure augmented scale with an unstable tonic.
    Notice that the Enigmatic Scale are played differently, with one variation, ascending and descending.
    """

    _modes_dict = {
        'major'              : [wholeStep, wholeStep, halfStep, wholeStep, wholeStep, wholeStep, halfStep],
        'ionian'             : [wholeStep, wholeStep, halfStep, wholeStep, wholeStep, wholeStep, halfStep],
        'dorian'             : [wholeStep, halfStep, wholeStep, wholeStep, wholeStep, halfStep, wholeStep],
        'phrygian'           : [halfStep, wholeStep, wholeStep, wholeStep, halfStep, wholeStep, wholeStep],
        'lydian'             : [wholeStep, wholeStep, wholeStep, halfStep, wholeStep, wholeStep, halfStep],
        'mixolydian'         : [wholeStep, wholeStep, halfStep, wholeStep, wholeStep, halfStep, wholeStep],
        'minor'              : [wholeStep, halfStep, wholeStep, wholeStep, halfStep, wholeStep, wholeStep],
        'locrian'            : [halfStep, wholeStep, wholeStep, halfStep, wholeStep, wholeStep, wholeStep],
        'aeolian'            : [wholeStep, halfStep, wholeStep, wholeStep, halfStep, wholeStep, wholeStep],
        'minor_blues'        : [wholeAndhalfStep, wholeStep, halfStep, halfStep, wholeAndhalfStep, wholeStep],
        'major_blues'        : [wholeStep, halfStep, halfStep, wholeAndhalfStep, wholeStep, wholeStep, halfStep],
        'melodic_minor'      : [wholeStep, halfStep, wholeStep, wholeStep, wholeStep, wholeStep, halfStep],
        'jazz_melodic_minor' : [wholeStep, halfStep, wholeStep, wholeStep, wholeStep, wholeStep, halfStep],
        'bebop_major'        : [wholeStep, wholeStep, halfStep, wholeStep, halfStep, halfStep, wholeStep, halfStep],
        'bebop_minor'        : [wholeStep, halfStep, halfStep, halfStep, wholeStep, wholeStep, halfStep, wholeStep],
        'bebop_dom'          : [wholeStep, wholeStep, halfStep, wholeStep, wholeStep, halfStep, halfStep, halfStep],
        'super_locrian'      : [halfStep, wholeStep, halfStep, wholeStep, wholeStep, wholeStep, wholeStep],
        'nine_tone'          : [wholeStep, halfStep, halfStep, wholeStep, halfStep, halfStep, halfStep, wholeStep,
                                halfStep],
        'bebop_dorian'       : [wholeStep, halfStep, halfStep, wholeStep, wholeStep, halfStep, wholeStep, halfStep],
        'pentatonic_minor'   : [wholeAndhalfStep, wholeStep, wholeStep, wholeAndhalfStep, wholeStep],
        'pentatonic_major'   : [wholeStep, wholeStep, wholeAndhalfStep, wholeStep, wholeAndhalfStep],
        'algerian_short'     : [wholeStep, halfStep, wholeStep, halfStep, halfStep, halfStep, wholeAndhalfStep,
                                wholeStep],
        'byzantine'          : [halfStep, wholeAndhalfStep, halfStep, wholeStep, halfStep, wholeAndhalfStep, halfStep],
        'algerian_long'      : [wholeStep, halfStep, wholeAndhalfStep, halfStep, halfStep, halfStep, wholeAndhalfStep,
                                wholeStep, wholeStep, halfStep, wholeStep],
        'arabic'             : [wholeStep, wholeStep, halfStep, halfStep, wholeStep, wholeStep, wholeStep],
        'augmented'          : [wholeAndhalfStep, halfStep, wholeAndhalfStep, halfStep, wholeAndhalfStep, halfStep],
        'balinese'           : [halfStep, wholeStep, quadraStep, halfStep, quadraStep],
        'chinese'            : [quadraStep, wholeStep, halfStep, quadraStep, halfStep],
        'diminished'         : [wholeStep, halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep, halfStep],
        'dim_blues'          : [halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep],
        'egyptian'           : [wholeStep, wholeAndhalfStep, wholeStep, wholeAndhalfStep, wholeStep],
        'eight_tone_spanish' : [halfStep, wholeStep, halfStep, halfStep, halfStep, wholeStep, wholeStep, wholeStep],
        'enigmatic_major'    : [halfStep, wholeAndhalfStep, wholeStep, wholeStep, wholeStep, wholeStep, halfStep,
                                halfStep],
        'enigmatic_minor'    : [halfStep, wholeStep, wholeAndhalfStep, halfStep, wholeAndhalfStep, halfStep, halfStep],
        'ethiopian'          : [wholeStep, halfStep, wholeStep, wholeStep, halfStep, wholeStep, wholeStep],
        'hindu'              : [wholeStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep, wholeStep],
        'hirajoshi'          : [halfStep, quadraStep, halfStep, quadraStep, wholeStep],
        'hungarian_gypsy'    : [wholeStep, halfStep, wholeAndhalfStep, halfStep, halfStep, wholeAndhalfStep, halfStep],
        'hungarian_major'    : [wholeAndhalfStep, halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep],
        'japanese'           : [halfStep, quadraStep, wholeStep, wholeAndhalfStep, wholeStep],
        'lydian_b7'          : [wholeStep, wholeStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep],
        'neapolitan_minor'   : [halfStep, wholeStep, wholeStep, wholeStep, halfStep, wholeAndhalfStep, halfStep],
        'neapolitan_major'   : [halfStep, wholeStep, wholeStep, wholeStep, wholeStep, wholeStep, halfStep],
        'octatonic_wholeHalf': [wholeStep, halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep, halfStep],
        'octatonic_halfWhole': [halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep, halfStep, wholeStep],
        'oriental'           : [halfStep, wholeAndhalfStep, halfStep, halfStep, wholeAndhalfStep, halfStep, wholeStep],
        'prometheus'         : [wholeStep, wholeStep, wholeStep, wholeAndhalfStep, halfStep, wholeStep],
        'whole_tone'         : [wholeStep, wholeStep, wholeStep, wholeStep, wholeStep, wholeStep],
        'romanian_minor'     : [wholeStep, halfStep, wholeAndhalfStep, halfStep, wholeStep, halfStep, wholeStep],
        'phrygian_dominant'  : [halfStep, wholeAndhalfStep, halfStep, wholeStep, halfStep, wholeStep, wholeStep],
        'yo'                 : [wholeStep, wholeAndhalfStep, wholeStep, wholeStep, wholeAndhalfStep],
        'custom'             : [wholeStep, halfStep, wholeStep, wholeStep, wholeAndhalfStep, wholeStep]
    }

    scale_dict = {}

    def __init__(self, key_sign):
        Interval.__init__(self, key_sign)
        self.mode = 'major'
        try:
            if len(self.key) > 1:
                if self.key[1] == 'm':
                    self.mode = 'minor'
                elif self.key[2] == 'm':
                    self.mode = 'minor'
        except IndexError:
            pass
        except AttributeError:
            pass

    def get_scale(self, param):
        """Returns all the valid notes in the Key Signature"""

        scale_step = self._modes_dict[param]
        modal_sign = get_key(self._modes_dict, scale_step)
        if (self.root + '_' + modal_sign) not in self.scale_dict:
            my_notes = applyEach(scale_step, self.root)
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
                        new_note = convert(my_notes[i])
                        my_notes[i] = new_note
                        if my_notes[i][0] in semantics.keys():
                            check_note = semantics[my_notes[i][0]]
                            first_char.append(check_note)
            except IndexError:
                pass

            finally:
                my_notes.pop()
                first_char.clear()
                self.scale_dict.update({(self.root + '_' + modal_sign): my_notes})
                # print(self.scale_dict)
        else:
            return self.scale_dict.get((self.root + '_' + modal_sign))

        return my_notes

    def get_notes(self):
        """return a list of all the notes in the Key Signature"""
        return self.get_scale(self.mode)

    def get_relativeScales(self):
        """ Get the closest scale that might work for improvising over a chord progression Takes no arguments.
        Returns a list of scale names which has the all the notes from its major or minor pentatonic scales. i.e; The the
        musical key is set as A, then it will show you all the scale names which has the notes from A major
        pentatonic scale. """
        list_one = []
        if self.mode == 'major':
            list_one = self.get_scale('pentatonic_major')
        else:
            list_one = self.get_scale('pentatonic_minor')
        x = list_one
        main_x = set(flats_to_sharps(x))
        list_two = []
        for key, val in self.scale_dict.items():
            if len(self.root) == 1:
                if key[0] == self.root:
                    y = val
                    main_y = set(flats_to_sharps(y))
                    if main_x.issubset(main_y) and key[1] == '_':
                        list_two.append(key)
            else:
                if key[0:2] == self.root:
                    y = val
                    main_y = set(flats_to_sharps(y))
                    if main_x.issubset(main_y):
                        list_two.append(key)

        return list_two[:]

    @classmethod
    def get_modes_dict_keys(cls):
        return cls._modes_dict.keys()


scale_list = Scale.get_modes_dict_keys()

for note in CHROMATICSCALE:
    x = Scale(note)
    for i in scale_list:
        x.get_scale(i)

# print(Scale.scale_dict)
