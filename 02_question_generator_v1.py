import random


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
elif choose_level == 2:
    l2num1, l2num2 = distribute_level(choose_level)
elif choose_level == 3:
    l3num1, l3num2 = distribute_level(choose_level)
else:
    print("Invalid level chosen.")
