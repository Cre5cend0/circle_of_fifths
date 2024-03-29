""" Musical Notes """
from circle_of_fifths import settings

CHROMATICSCALE = (
    'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g',
    'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#',
    'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b',
    'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g',
    'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#',
    'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b',
    'c', 'Db', 'd', 'Eb', 'e', 'f', 'Gb', 'g',
    'Ab', 'a', 'Bb', 'b', 'c', 'Db', 'd', 'Eb',
    'e', 'f', 'Gb', 'g', 'Ab', 'a', 'Bb', 'b',
    'c', 'Db', 'd', 'Eb', 'e', 'f', 'Gb', 'g',
    'Ab', 'a', 'Bb', 'b', 'c', 'Db', 'd', 'Eb',
    'e', 'f', 'Gb', 'g', 'Ab', 'a', 'Bb', 'b',
)

CHROMATICSCALE_SHARPS = ('c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g',
                         'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#',
                         'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b',
                         'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g',
                         'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#',
                         'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b')

CHROMATICSCALE_FlATS = ('c', 'Db', 'd', 'Eb', 'e', 'f', 'Gb', 'g',
                        'Ab', 'a', 'Bb', 'b', 'c', 'Db', 'd', 'Eb',
                        'e', 'f', 'Gb', 'g', 'Ab', 'a', 'Bb', 'b',
                        'c', 'Db', 'd', 'Eb', 'e', 'f', 'Gb', 'g',
                        'Ab', 'a', 'Bb', 'b', 'c', 'Db', 'd', 'Eb',
                        'e', 'f', 'Gb', 'g', 'Ab', 'a', 'Bb', 'b')

circle_of_fifths_mj = ('Gb', 'Db', 'Ab', 'Eb', 'Bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b',
                       'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b',
                       'f#', 'c#', 'g#', 'd#', 'a#', 'f', 'c', 'g', 'd', 'a', 'e', 'b',
                       'f#', 'c#', 'g#', 'd#', 'a#', 'f', 'c', 'g', 'd', 'a', 'e', 'b')

circle_of_fifths_mi = ('d#m', 'a#m', 'fm', 'cm', 'gm', 'dm', 'am', 'em', 'bm', 'f#m', 'c#m', 'g#m',
                       'd#m', 'a#m', 'fm', 'cm', 'gm', 'dm', 'am', 'em', 'bm', 'f#m', 'c#m', 'g#m',
                       'Ebm', 'Bbm', 'fm', 'cm', 'gm', 'dm', 'am', 'em', 'bm', 'Gbm', 'Dbm', 'Abm',
                       'Ebm', 'Bbm', 'fm', 'cm', 'gm', 'dm', 'am', 'em', 'bm', 'Gbm', 'Dbm', 'Abm')

accidentals = {
    'c#': 'Db', 'Db': 'c#', 'd#': 'Eb', 'Eb': 'd#', 'f#': 'Gb', 'Gb': 'f#', 'g#': 'Ab', 'Ab': 'g#',
    'a#': 'Bb', 'Bb': 'a#', 'Cb': 'b', 'b': 'Cb', 'e#': 'f', 'f': 'e#', 'b#': 'c',
    'e' : 'Fb', 'Fb': 'e'
}

semantics = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g'}

chrom_exec = []


def setup(pref):
    # print('setting up...')  # todo remove line once done
    global chrom_exec
    if pref == 'flats':
        for item in CHROMATICSCALE_FlATS:
            chrom_exec.append(item)
    elif pref == 'sharps':
        for item in CHROMATICSCALE_SHARPS:
            chrom_exec.append(item)

    if pref is not None:  # todo
        from circle_of_fifths.core_files.scales import Scale
        scale_list = Scale.get_modes_dict_keys()

        for note in chrom_exec:
            x = Scale(note)
            for i in scale_list:
                x.get_scale(i)

        from circle_of_fifths.core_files.chords import Chord
        from circle_of_fifths.utilities.func_tools import applyAll

        y = Chord.get_chord_list()
        for item in chrom_exec:
            x = Chord(item)
            applyAll(x.chordGen, y)

    # print(f'Accidental preference is set to {pref}')
    return


def pref_finder():
    if settings.pref is None:
        local_pref = None
        try:
            if settings.my_key.getKey() in ['Bb', 'Cb', 'Db', 'Eb', 'Ab', 'Gb', 'Fb', 'f', 'gm', 'cm', 'dm', 'fm',
                                            'Bbm', 'Ebm']:
                local_pref = 'flats'
            elif settings.my_key.getKey() in ['c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#', 'am', 'em',
                                              'bm',
                                              'f#m', 'c#m', 'g#m', 'd#m']:
                local_pref = 'sharps'
        except IndexError:
            pass
        except AttributeError:
            pass
        finally:
            setup(local_pref)

    else:
        setup(settings.pref)

    return


pref_finder()


def halfStep(note):
    """takes one string argument: note -> Any valid musical note
    returns next half step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index + 1]


def wholeStep(note):
    """takes one string argument: note -> Any valid musical note
    returns next whole step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index + 2]


def wholeAndhalfStep(note):
    """takes one string argument: note -> Any valid musical note
    returns next half step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index + 3]


def quadraStep(note):
    """takes one string argument: note -> Any valid musical note
    returns next half step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index + 4]


def wholeAndhalfStep_lower(note):
    """takes one string argument: note -> Any valid musical note
    returns next whole step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index - 3]


def halfSteplower(note):
    """takes one string argument: note -> Any valid musical note
    returns previous half step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index - 1]


def wholeSteplower(note):
    """takes one string argument: note -> Any valid musical note
    returns previous whole step note"""
    index = chrom_exec.index(note)
    return chrom_exec[index - 2]
