""" Musical Notes """
import settings

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
    print('setting up...')  # todo remove line once done
    global chrom_exec
    global CHROMATICSCALE_SHARPS
    global CHROMATICSCALE_FlATS
    if pref == 'flats':
        chrom_exec = CHROMATICSCALE_FlATS[:]
    elif pref == 'sharps':
        chrom_exec = CHROMATICSCALE_SHARPS[:]
    else:
        chrom_exec = CHROMATICSCALE[:]
    # print(f'Accidental preference is set to {pref}')
    return


def pref_finder():
    if settings.pref is None:
        local_pref = None
        try:
            if settings.my_key.getKey() in ['Bb', 'Cb', 'Db', 'Eb', 'Ab', 'Gb', 'Fb', 'f', 'gm', 'cm', 'dm', 'fm', 'Bbm', 'Ebm']:
                local_pref = 'flats'
            elif settings.my_key.getKey() in ['c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#', 'am', 'em', 'bm',
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
