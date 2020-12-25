""" a decorator function for outputs"""

# Decorator function
# probably more userful for displaying fretboard than outputs


def deco(func):
    def wrap_func(*args, **kwargs):
        print('_' * 173)
        func(*args, **kwargs)
    return wrap_func

