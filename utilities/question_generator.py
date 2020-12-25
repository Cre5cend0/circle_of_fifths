# """A blueprint for creating questions for Interact"""
# todo

import utilities.sequence as seq
import subprocess


class Question():
    '''Takes no arguments. default attr skip -> 'no' and response -> None'''

    def __init__(self):
        self.skip = 'no'
        self.response = None

    def funcGen(self, name, query):
        '''a function generator
        Takes two arguments.
        name: Name of the func
        query: Question to be asked
        '''
        if self.skip == 'no':
            # ask question
            self.response = interact.interact(query)
        else:
            # continue to perform action
            self.response = True

        return


"""A blueprint for creating questions for Interact"""
import interact
import utilities.sequence

QUESTIONS_DICT = {
    1: 'Would you like to view the chords? ',
    2: 'Show maj7? ',
    3: 'Like it so far? '
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

    def gen(self, query, skip='no'):
        '''a function generator
        Takes one argument.
        query: Question to be asked
        '''

        if skip == 'no':
            # ask question
            self.response = interact.interact(query)
        else:
            # continue to perform action
            self.response = True

        if self.response:
            p1 = subprocess.call('responses')

        else:
            seq.sequencer([self(ques(self.q_no - 1)), self(ques(self.q_no))])

        return self.response

    def __call__(self, *args, **kwargs):
        return self.gen(*args, **kwargs)

    def __str__(self):
        pass
