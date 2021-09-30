import random

import settings


def fret_range(capo, start=0, stop=settings.my_neck, step=1):

    num1 = 0
    num2 = 0

    def numgen(capo):
        stop = settings.my_neck - capo
        num1 = random.randrange(start, stop, step)
        num2 = random.randrange(start, stop, step)
        return num1, num2

    while True:
        if (num1 < num2) and ((num2 - num1) == 4):
            break
        else:
            num1, num2 = numgen(capo)
    return num1, num2
