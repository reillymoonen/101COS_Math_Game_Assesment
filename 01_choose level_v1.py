# Functions
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


# Main routine
choose_level = num_check("What Level would you like to play"
                         " (1, 2, 3)\n", 0, 3)
# Print the output
print("You have selected level {}".format(choose_level))
