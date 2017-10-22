import feedback

def main():
    # print_error
    print("Testing 'feedback.print_error'")
    feedback.print_error("Everything has gone wrong, abort!")
    print()

    # task
    print("Testing 'feedback.Task'")
    task = feedback.Task("Transmuting straw to gold")
    print()

    # task starting
    print("Testing 'task.start()'")
    task.start()
    print()

    # task finished
    print("Testing 'task.success()'")
    task.success()
    print()

    # task error
    print ("Testing 'task.error()'")
    task.error("missing philosopher's stone")
    print()


if __name__ == "__main__":
    main()

