from circle_of_fifths.core_files.musicalNotes import chrom_exec, CHROMATICSCALE


class Interval:

    def __init__(self, key_sign):
        try:
            try:
                self.root = key_sign
                if len(key_sign) > 1:
                    if key_sign[1] == 'm':
                        self.root = key_sign[:1]
                    elif key_sign[2] == 'm':
                        self.root = key_sign[:2]
            except IndexError:
                pass

            if self.root in CHROMATICSCALE:
                self.key = key_sign
            # elif self.root in accidentals:
            #     self.key = accidentals[key_sign]
            else:
                raise KeyError
        except KeyError:
            print('''
            Key error: Root note not available. 
            Please ensure that you are following standard naming convention as follows:
            All key names are lowercase letters except Key signatures with flats(b) in them.
            see below:
            E major can simply be written as 'e' without the quotes. 
            E sharp can be written as 'e#' without the quotes.
            E flat major key can be written as 'Eb' without the quotes.
            E flat minor key can be written as 'Ebm' without the quotes.
            Use Alphabet 'b' to denote flat keys and '#' to denote sharp keys.
            Or, Try an alternative name of the key such as E major can be written as Fb
                     '''
                  )
            raise KeyError

    def getRoot(self):
        return self.root

    def getKey(self):
        return self.key

    def m2(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index + 1]

    def M2(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index + 2]

    def m3(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index + 3]

    def M3(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index + 4]

    def P4(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index + 5]

    def tritone(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index + 6]

    def b5(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index - 6]

    def P5(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index - 5]

    def m6(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index - 4]

    def M6(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index - 3]

    def m7(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index - 2]

    def M7(self):
        index = chrom_exec.index(self.root)
        return chrom_exec[index - 1]

    def octave(self):
        return self.root

    def unison(self):
        return self.root

    def get_blues(self):
        return self + b5

    def get_tension(self):
        return self + m2, self + tritone, self + M7

    def get_anticipation(self):
        return self + M2, self + m3, self + P4, self + m7

    def get_resolution(self):
        return self + unison, self + M3, self + P5, self + octave

    def get_sensation(self):
        return self + M6, self + m6

    def __add__(self, scale_step):
        return scale_step(self)


m2 = Interval.m2
M2 = Interval.M2
m3 = Interval.m3
M3 = Interval.M3
P4 = Interval.P4
b5 = Interval.b5
tritone = Interval.tritone
P5 = Interval.P5
m6 = Interval.m6
M6 = Interval.M6
m7 = Interval.m7
M7 = Interval.M7
octave = Interval.octave
unison = Interval.unison
