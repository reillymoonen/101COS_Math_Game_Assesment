# Functions
def yes_no(questions):
    valid = False
    while not valid:
        response = input("Have you played this game "
                         "before?").lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Main Routine

show_instructions = yes_no("Have you played the "
                           "game before?")
print("You choose {}".format(show_instructions))
