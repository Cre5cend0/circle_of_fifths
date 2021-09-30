import types
import settings

from utilities.inputs import inputChecker


def feedback(question, comment):
    with open('feedback.txt', 'a')as file:
        file.write(question + ':' + comment + '\n')
    return


response = None


def interact(question):
    '''
    Takes one argument. A question.
    Returns user_input if valid, else, adds it to feedback list and raise ValueError
    '''
    global response
    query = question
    while True:
        if not settings.user_turn:
            # response is the Input received from the user
            response = input(query)
        try:
            # result is the parsed value of the user response for computer to interpret and perform operations
            result = inputChecker(response)
            if result == 0:
                return False
            elif result == 1:
                return True
            elif result == 2:
                return None
            elif result is None:
                response = 'my turn'
            elif result == 7:
                settings.user_turn = False
                continue
            elif result == response:
                return response
            elif result == ValueError:
                raise ValueError
            elif isinstance(result, str):
                # happens when user tries to switch control of the console by using keyword 'my turn'
                response = result
                settings.user_turn = True
        except ValueError:
            print("Invalid input. Type 'help' command if you\'re having trouble.")
            if settings.user_turn:
                response = 'my turn'
            print()
            feedback(question, response)
