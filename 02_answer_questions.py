import random


def question_solver(num1, num2):
    correct_answer = num1 + num2
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Sorry the correct answer is {correct_answer}.")


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


choose_level = int(input("which level do you want from 1 to 3"))
if choose_level == 1:
    l1num1, l1num2 = distribute_level(choose_level)
    question_solver(l1num1, l1num2)
elif choose_level == 2:
    l2num1, l2num2 = distribute_level(choose_level)
    question_solver(l2num1, l2num2)
elif choose_level == 3:
    l3num1, l3num2 = distribute_level(choose_level)
    question_solver(l3num1, l3num2)
