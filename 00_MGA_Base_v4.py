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
            print("\033[1;33m1. Choose Your Level: You will be prompted to select a difficulty level (1, 2, "
                  "or 3) at the beginning of each game.")
            print("2. Solve the Questions: You will be presented with a series of addition questions based on your "
                  "chosen level. Input your answer and press Enter.")
            print("3. Check Your Answer: The game will let you know if your answer is correct or not.")
            print("4. Game Summary: After completing the questions, a game summary will show your total questions, "
                  "correct answers, and accuracy percentage.")
            print("5. Play Again: You have the option to play again or exit the game.\033[1;36m")
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
                print("\033[1;32m╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
                print("║║ ! Correct ! ║║")
                print("╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝ \033[1;36m")
                print()
                return True
            else:
                print("\033[1;31m╔╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
                print("║║ ! Wrong ! ║║")
                print("╚╩╩╩╩╩╩╩╩╩╩╩╩╩╝")
                print(f"The correct answer is {correct_answer}. \033[1;36m")
                return False
        else:
            print("Please enter a valid numeric answer.")


def game_summary(correct_answers, total_questions):
    print("\nGame Summary:")
    print("---------------")
    print(f"Total questions: {total_questions}")
    print(f"Correct answers: {correct_answers}")
    accuracy = (correct_answers / total_questions) * 100
    print(f"Accuracy: {accuracy:.0f}%")
    print()


def play_again(question):
    valid = False
    while not valid:
        response = input(question).lower()
        error = "Please answer yes / no"

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print(error)


# Main Routine
print("\033[1;36mWelcome to the Math Challenge Game! In this game, you will be presented with addition questions of "
      "different ")
print("difficulty levels. Your task is to solve these questions as accurately as possible.")
print()
show_instructions = yes_no("Have you played the "
                           "game before?\n")
while True:
    print()
    choose_level = num_check("What Level would you like to play"
                             " (1, 2, 3)\n", 1, 3)
    print("You have selected level {}".format(choose_level))
    print()

    correct_answers = 0
    total_questions = 10
    first_question = 1
    current_question = 2

    if choose_level == 1:
        print("Question", format(first_question))
        for _ in range(total_questions):
            l1num1, l1num2 = distribute_level(choose_level)
            if question_solver(l1num1, l1num2):
                print("Question", format(current_question))
                correct_answers += 1
                current_question += 1
            else:
                print()
                print("Question", format(current_question))
                current_question += 1
        else:
            print("Invalid level chosen.")

    elif choose_level == 2:
        print("Question", format(first_question))
        for _ in range(total_questions):
            l1num1, l1num2 = distribute_level(choose_level)
            if question_solver(l1num1, l1num2):
                print("Question", format(current_question))
                correct_answers += 1
                current_question += 1
            else:
                print()
                print("Question", format(current_question))
                current_question += 1
        else:
            print("Invalid level chosen.")

    elif choose_level == 3:
        print("Question", format(first_question))
        for _ in range(total_questions):
            l1num1, l1num2 = distribute_level(choose_level)
            if question_solver(l1num1, l1num2):
                print("Question", format(current_question))
                correct_answers += 1
                current_question += 1
            else:
                print()
                print("Question", format(current_question))
                current_question += 1
        else:
            print("Invalid level chosen.")

    game_summary(correct_answers, total_questions)

    replay = play_again("Would you like to play again? (yes/no)\n")
    if replay != "yes":
        print()
        print("\033[1;34m╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
        print("║║ X Game Closed X ║║")
        print("╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝\033[1;36m")

        break
