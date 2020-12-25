from core_files.musicalKeys import *
import time
from core_files.musicalNotes import *

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
    time.sleep(3)
