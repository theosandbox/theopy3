import user_input

def main():
    # get yes/no
    print("Testing 'get_user_confirmation'")
    result = user_input.get_user_confirmation("Would you like to turn dust to gold?")
    print("Result: {0}".format(result))

if __name__ == "__main__":
    main()