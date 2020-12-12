from musicalNotes import accidentals

"""applyEach"""

_flats_to_sharps = {'Db': 'c#', 'Eb': 'd#', 'Gb': 'f#', 'Ab': 'g#', 'Bb': 'a#', 'Cb': 'b', 'Fb': 'e'}

_sharps_to_flats = {'c#': 'Db', 'd#': 'Eb', 'f#': 'Gb', 'g#': 'Ab', 'a#': 'Bb', 'e#': 'f', 'b#': 'c'}


def applyEach(funcs, param):
    """Takes a list of functions and a param as argument and for each function f in the list, returns f(params) as a
    list"""
    li = []
    for func in funcs:
        result = func(param)
        li.append(result)
        param = result
    return li[:]


def applyAll(func, params, **kwargs):
    """Takes a function and a list of params as argument and for each param p in the list, returns function(p) as a
    list"""
    li = []
    for param in params:
        result = func(param, **kwargs)
        li.append(result)
    return li[:]


def runMethod(obj, methods):
    """Takes an object and a list of methods as argument. Applies each method to the object and returns results in a
    list"""
    li = []
    for method in methods:
        result = method(obj)
        li.append(result)
    return li[:]


def get_key(my_dict, val):
    """function to return key for any value"""
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def convert(note):
    if note in accidentals.keys():
        similar_note = accidentals.get(note)
    else:
        similar_note = note

    return similar_note


def flats_to_sharps(note_bunch):
    temp_bunch = note_bunch[:]
    for i in range(len(temp_bunch)):
        if temp_bunch[i] in _flats_to_sharps.keys():
            temp_bunch.pop(i)
            temp_bunch.insert(i, _flats_to_sharps.get(note_bunch[i]))
    return temp_bunch[:]
