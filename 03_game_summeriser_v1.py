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


correct_answers = 0
total_questions = 10

game_summary(correct_answers, total_questions)
