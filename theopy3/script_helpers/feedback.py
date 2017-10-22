import sys
from colorama import Back, Fore


_TAG_WIDTH = 22

def print_error(error_msg):
    print(_format_msg("ERROR", Back.RED) + error_msg)

def print_input_prompt(prompt_msg, prompt):
    sys.stdout.write(_format_msg("Input required", Back.CYAN) + prompt_msg + prompt)

class Task:
    """
    Allows ways to give easy feedback to the user about the status of script tasks.
    """

    def __init__(self, task_name):
        self.task_name = task_name
    
    def start(self):
        """
        Give feedback that the task has started
        """
        print(_format_msg("Starting task", Back.LIGHTCYAN_EX, Fore.BLACK) + self.task_name)
    
    def success(self):
        """
        Give feedback that the task was successful
        """
        print(_format_msg("Task successful", Back.GREEN) + "({0})".format(self.task_name)) 
    
    def error(self, error_msg):
        """
        Give feedback that the task failed
        """
        print(_format_msg("Task failed", Back.RED) + "({0})".format(self.task_name))
        print(" " * _TAG_WIDTH + "\t   " + error_msg)

def _format_msg(msg, back_color=Back.RESET, fore_color=Fore.RESET):
    # do padding
    new_msg = "{0}{1}  {2}  {3}{4}".format(back_color, fore_color, msg, Back.RESET, Fore.RESET)
    proper_msg_length = len(msg) + 4
    padding = " " * (_TAG_WIDTH - proper_msg_length)
    return "{0}{1}".format(new_msg, padding)