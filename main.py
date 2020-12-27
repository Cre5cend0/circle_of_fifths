from core_files.musicalKeys import *
import time
from core_files.musicalNotes import *
from utilities.question_generator import ques, Question
from core_files.fretboard import fretGen

if __name__ == '__main__':
    print()


    def start(skip='no'):
        response = None
        while True:
            try:
                settings.my_key = Key(input('Hi! Choose a musical Key: '))
                pref_finder()
                if settings.my_key:
                    print()
                    print(f'Great choice! Here are the notes from this key signature: ', end='')
                    notes = settings.my_key.get_notes()
                    for i in notes:
                        print(i, end=' ')
                    time.sleep(5)
                    print()
                    print('Hope you memorised them')
                    break
            except ValueError:
                continue
            finally:
                print('\n')

        return


    start()

    # Asking question 1 from question_dict
    ques_one = Question.gen(ques(1))

    if ques_one:
        print("Here's some major chords")
        settings.my_key.maj_triads(is_chord=True)
    elif ques_one is None:
        pass

    ques_two = Question.gen(ques(2))

    if ques_two:
        try:
            chord = settings.my_key.suggest_bar_chords_prog()
            fretGen(next(chord))
        except StopIteration:
            pass
    elif ques_one is None:
        pass

    ques_three = Question.gen(ques(3))

    if ques_three:
        print('awesome')
    elif ques_one is None:
        pass
