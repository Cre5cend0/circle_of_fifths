import time


def sequencer(list_of_requests):
    '''
    Takes a list of funcs. For each func in list, calls func(skip)  with 3 sec delay
    skip --> Skips the initial input request if Yes.
    Automatically detects the last func to run, and changes skip to 'no'.
    '''
    for i in range(len(list_of_requests)):
        skip = 'yes'
        if i == (len(list_of_requests) - 1):
            skip = 'no'
            return list_of_requests[i](skip)
        else:
            list_of_requests[i](skip)
            time.sleep(3)
