"""A timer function to schedule events and run based off time elapsed since the last program"""

import time
from threading import Timer


def schedule_an_event(sec, func):
    Timer(sec, func).start()
