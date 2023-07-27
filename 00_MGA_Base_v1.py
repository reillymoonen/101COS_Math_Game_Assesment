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


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 3\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine

show_instructions = yes_no("Have you played the "
                           "game before?")
print("You choose {}".format(show_instructions))
choose_level = num_check("What Level would you like to play"
                         " (1, 2, 3)\n", 0, 3)
print("You have selected level {}".format(choose_level))
