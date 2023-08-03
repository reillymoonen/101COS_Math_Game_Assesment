import random


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
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
    error = f"Please enter a whole number between {low} and {high}\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
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
    number_a = random.randint(10, 99)
    number_b = random.randint(10, 99)
    print(f"What is {number_a} + {number_b}?")
    return number_a, number_b


def level_3_generator():
    number_a = random.randint(100, 999)
    number_b = random.randint(100, 999)
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
    while True:
        user_answer = input("Your answer: ")
        if user_answer.isdigit():
            if int(user_answer) == correct_answer:
                print("Correct!")
                return True
            else:
                print(f"Sorry, the correct answer is {correct_answer}.")
                return False
        else:
            print("Please enter a valid numeric answer.")


def game_summary(correct_answers, total_questions):
    print("\nGame Summary:")
    print("---------------")
    print(f"Total questions: {total_questions}")
    print(f"Correct answers: {correct_answers}")
    accuracy = (correct_answers / total_questions) * 100
    print(f"Accuracy: {accuracy:.2f}%")


# Main Routine
show_instructions = yes_no("Have you played the "
                           "game before?\n")
choose_level = num_check("What Level would you like to play"
                         " (1, 2, 3)\n", 0, 3)
print("You have selected level {}".format(choose_level))
print()

correct_answers = 0
total_questions = 10

if choose_level == 1:
    for _ in range(total_questions):
        l1num1, l1num2 = distribute_level(choose_level)
        if question_solver(l1num1, l1num2):
            correct_answers += 1
    else:
        print("Invalid level chosen.")
elif choose_level == 2:
    for _ in range(total_questions):
        l2num1, l2num2 = distribute_level(choose_level)
        if question_solver(l2num1, l2num2):
            correct_answers += 1
    else:
        print("Invalid level chosen.")
elif choose_level == 3:
    for _ in range(total_questions):
        l3num1, l3num2 = distribute_level(choose_level)
        if question_solver(l3num1, l3num2):
            correct_answers += 1
    else:
        print("Invalid level chosen.")

game_summary(correct_answers, total_questions)
