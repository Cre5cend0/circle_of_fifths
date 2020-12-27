from utilities.inputs import inputChecker


def feedback(question, comment):
    file = open('feedback.txt', 'a')
    file.write(question + ':' + comment + '\n')


def interact(question):
    '''
    Takes one argument. A question.
    Returns user_input if valid, else, adds it to feedback list and raise ValueError
    '''
    while True:
        response = input(question)
        try:
            result = inputChecker(response)
            if result == 10:
                return True
            elif result == 5:
                return False
            elif result == 2:
                return None
            elif result == response:
                return response
            elif result == ValueError:
                raise ValueError
        except ValueError:
            print("Invalid input. Type 'help' command if you\'re having trouble.")
            print()
            feedback(question, response)
