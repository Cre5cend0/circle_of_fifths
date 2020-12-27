import types

from utilities.inputs import inputChecker


def feedback(question, comment):
    with open('feedback.txt', 'a')as file:
        file.write(question + ':' + comment + '\n')
    return


user_turn = False
response = None


def interact(question):
    '''
    Takes one argument. A question.
    Returns user_input if valid, else, adds it to feedback list and raise ValueError
    '''
    global user_turn
    global response
    query = question
    while True:
        if not user_turn:
            response = input(query)
        try:
            result = inputChecker(response)
            if result == 10:
                return True
            elif result == 5:
                return False
            elif result == 2:
                return None
            elif result == 7:
                user_turn = False
                continue
            elif result == response:
                return response
            elif result == ValueError:
                raise ValueError
            elif isinstance(result, str):
                response = result
                user_turn = True
        except ValueError:
            print("Invalid input. Type 'help' command if you\'re having trouble.")
            if user_turn:
                response = 'my turn'
            print()
            feedback(question, response)

