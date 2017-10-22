from colorama import Back, Fore

def print_error(error_msg):
    print(Back.RED + "  ERROR  "  + Back.RESET + " " + error_msg)

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
        print(Back.LIGHTCYAN_EX + Fore.BLACK + "  Starting task  " + Back.RESET + Fore.RESET + " " + self.task_name)
    
    def success(self):
        """
        Give feedback that the task was successful
        """
        print(Back.GREEN + "  Task successful  "  + Back.RESET + Fore.RESET + " ({0})".format(self.task_name)) 
    
    def error(self, error_msg):
        """
        Give feedback that the task failed
        """
        print(Back.RED + "  Task failed  " + Back.RESET + " ({0})".format(self.task_name))
        print("\t\t" + error_msg)
