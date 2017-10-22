import sys

import feedback

def get_user_confirmation(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.
    
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is a bool (True for "yes", False for "no")
    """
    yes_options = ["yes", "y"]
    no_options = ["no", "n"]
    
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        feedback.print_input_prompt(question, prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return default == "yes"
        elif choice in yes_options:
            return True
        elif choice in no_options:
            return False
        else:
            feedback.print_error("Please respond with 'yes' or 'no' (or 'y' or 'n')")