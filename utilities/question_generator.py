"""A blueprint for creating questions for Interact"""
import types

from utilities.sequence import sequencer as seq
import subprocess
from utilities.interact import interact

QUESTIONS_DICT = {
    1: 'Would you like to view the chords? ',
    2: 'Shall i show some chord progression? ',
    3: 'Want to view advanced chord progressions? ',
    4: 'Like it so far? '
}

TOPICS = (
    # todo
    # scales, modes, chords, intervals, chord progressions, notes, fret positions
)


def ques(num):
    return QUESTIONS_DICT[num]


class Question:
    '''Takes no arguments. default attr skip -> 'no' and response -> None'''
    q_no = 1

    def __init__(self):
        self.name = self.q_no
        self.q_no += 1
        self.response = None
        print(self.q_no)

    @classmethod
    def gen(cls, query, skip='no'):
        '''a function generator
        Takes one argument.
        query: Question to be asked
        '''

        if skip == 'no':
            # ask question
            cls.response = interact(query)
        else:
            # continue to perform action
            cls.response = True

        if cls.response is None:
            pass

        elif not cls.response:
            cls.response = cls.gen(query)
        #
        # else:
        #     seq([ques(cls.q_no - 1), ques(cls.q_no)])
        return cls.response

    def __call__(self, *args, **kwargs):
        return self.gen(*args, **kwargs)

    def __str__(self):
        pass
