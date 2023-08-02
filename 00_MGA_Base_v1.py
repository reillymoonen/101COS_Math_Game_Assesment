import random


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
            print()
            return response

        else:
            print(error)


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 3\n"

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


def level_1_generator():
    number_a = random.randint(1, 9)
    number_b = random.randint(1, 9)

    print(f"What is {number_a} + {number_b}?")
    return number_a, number_b


def level_2_generator():
    number_a = random.randint(1, 99)
    number_b = random.randint(1, 99)

    print(f"What is {number_a} + {number_b}?")
    return number_a, number_b


def level_3_generator():
    number_a = random.randint(1, 999)
    number_b = random.randint(1, 999)

    print(f"What is {number_a} + {number_b}?")
    return number_a, number_b


def distribute_level(level):
    if level == 1:
        return level_1_generator()
    elif level == 2:
        return level_2_generator()
    elif level == 3:
        return level_3_generator()


def question_solver(num1, num2):
    correct_answer = num1 + num2
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Sorry the correct answer is {correct_answer}.")


# Main Routine

show_instructions = yes_no("Have you played the "
                           "game before?\n")
choose_level = num_check("What Level would you like to play"
                         " (1, 2, 3)\n", 0, 3)
print("You have selected level {}".format(choose_level))
print()

if choose_level == 1:
    for _ in range(10):
        l1num1, l1num2 = distribute_level(choose_level)
        question_solver(l1num1, l1num2)
elif choose_level == 2:
    for _ in range(10):
        l2num1, l2num2 = distribute_level(choose_level)
        question_solver(l2num1, l2num2)
elif choose_level == 3:
    for _ in range(10):
        l3num1, l3num2 = distribute_level(choose_level)
        question_solver(l3num1, l3num2)
else:
    print("Invalid level chosen.")
