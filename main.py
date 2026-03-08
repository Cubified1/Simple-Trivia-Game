import random
import time


decor1 = "="
decor1_amount = 20
loading_prog = "."
loading_prog_rand = random.randint(2, 3)
guesses = []

print(decor1 * decor1_amount)
print ("welcome to my simple trivia game")
print(decor1 * decor1_amount)

print("loading", end=" ")
for load in range(3):
    time.sleep(1)
    loading_prog = loading_prog * loading_prog_rand
    print(loading_prog, end="")


time.sleep(2)

print("\n" * 3)

def sport():
    question_num = 0
    score = 0
    loading_result_rand = random.randint(2, 3)

    questions = ("How many players are on a basketball team on the court?: ",
                 "Which country invented basketball?: ",
                 "How many points is a touchdown worth in American football?: ",
                 "How many holes are in a standard golf round?: ",
                 "Which sport uses a puck?: ")


    options = (("(A) 4, (B) 5, (C) 6, (D) 7: "),
               ("(A) USA, (B) UK, (C) Canada, (D) Australia: "),
               ("(A) 3, (B) 6, (C) 7, (D) 8: "),
               ("(A) 9, (B) 12, (C) 18, (D) 24: "),
               ("(A) Lacrosse, (B) Hockey, (C) Polo, (D) Curling: "))

    answer = ("B", "C", "B", "C", "B")
    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option, end="")
        user_guess = input("\n").upper()
        guesses.append(user_guess)
        if user_guess == answer[question_num]:
            score += 1

            print("CORRECT!")

        else:
            print("WRONG!")

        question_num += 1

    print("\n")
    print("Culminating results")

    for loading_result in range(3):
        time.sleep(1)
        loading_result = loading_prog * loading_result_rand
        print(loading_result, end="")

    time.sleep(1)
    print("\n" * 2)
    print("Your score:", score)
    print("\n")

    time.sleep(1)

    if score == 5:
        print("WOW! ALL QUESTIONS CORRECT!")
        print("Get ready for more questions!")

    elif score == 1:
        print("You got 1 question correct!")
        print("Get ready for more questions!")

    elif score == 0:
        print("You got 0 questions correct")
        print("Get ready for more questions!")

    else:
        print(f"You got {score} questions correct!")
        print("Get ready for more questions!")


sport()