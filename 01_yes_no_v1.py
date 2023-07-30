# Functions
def yes_no(questions):
    valid = False
    while not valid:
        response = input(questions).lower()
        error = "Please answer yes / no"

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            print("Instructions")
            return response

        else:
            print(error)


# Main Routine

show_instructions = yes_no("Have you played the "
                           "game before?")
print("You choose {}".format(show_instructions))
