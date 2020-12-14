from musicalKeys import *
import time
from musicalNotes import *

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
                    print(f'Here are the notes from this key signature. Memorize them if you can.')
                    notes = settings.my_key.get_notes()
                    print()
                    for i in notes:
                        print(i, end=' ')
                    break
            except ValueError:
                continue
            finally:
                print('\n')

        return


    start()
    time.sleep(3)
