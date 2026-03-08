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
    sport_score = 0
    loading_result_rand = random.randint(2, 3)

    questions = ("How many players are on a basketball team on the court?: ",
                 "Which country invented basketball?: ",
                 "How many points is a touchdown worth in American football?: ",
                 "How many holes are in a standard golf round?: ",
                 "Which sport uses a puck?: ")


    options = ("(A) 4, (B) 5, (C) 6, (D) 7: ",
               "(A) USA, (B) UK, (C) Canada, (D) Australia: ",
               "(A) 3, (B) 6, (C) 7, (D) 8: ",
               "(A) 9, (B) 12, (C) 18, (D) 24: ",
               "(A) Lacrosse, (B) Hockey, (C) Polo, (D) Curling: ")

    answer = ("B", "C", "B", "C", "B")
    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option, end="")
        user_guess = input("\n").upper()
        guesses.append(user_guess)
        if user_guess == answer[question_num]:
            sport_score += 1

            print("CORRECT!")

        else:
            print("WRONG!")

        question_num += 1

    print("\n")
    print("Culminating results")

    for loading_result in range(3):
        time.sleep(1)
        loading_result = loading_prog * 1
        print(loading_result, end="")

    time.sleep(1)
    print("\n" * 2)
    print("Your score:", sport_score)
    print("\n")

    time.sleep(1)

    if sport_score == 5:
        print("WOW! ALL QUESTIONS CORRECT!")

    elif sport_score == 1:
        print("You got 1 question correct!")

    elif sport_score == 0:
        print("You got 0 questions correct")

    else:
        print(f"You got {sport_score} questions correct!")


def science():
    science_question_num = 0
    science_score = 0
    loading_result_rand = random.randint(2, 3)

    science_questions = ("What planet is closest to the sun?: ",
                 "What gas do plants absorb?: ",
                 "How many bones are in the human body?: ",
                 "What is the chemical symbol for gold?: ",
                 "What is the speed of light?: ")

    science_options = ("(A) Venus, (B) Earth, (C) Mars, (D) Mercury: ",
               "(A) Oxygen, (B) Nitrogen, (C) Carbon Dioxide, (D) Hydrogen: ",
               "(A) 196, (B) 206, (C) 216, (D) 226: ",
               "(A) Go, (B) Gd, (C) Gl, (D) Au: ",
               "(A) 300,000 km/s, (B) 150,000 km/s, (C) 500,000 km/s, (D) 1,000,000 km/s: ")

    science_answer = ("D", "C", "B", "D", "A")
    for question in science_questions:
        print(question)
        for option in science_options[science_question_num]:
            print(option, end="")
        user_guess = input("\n").upper()
        guesses.append(user_guess)
        if user_guess == science_answer[science_question_num]:
            science_score += 1

            print("CORRECT!")

        else:
            print("WRONG!")

        science_question_num += 1

    print("\n")
    print("Culminating results")

    for loading_result in range(3):
        time.sleep(1)
        loading_result = loading_prog * loading_result_rand
        print(loading_result, end="")

    time.sleep(1)
    print("\n" * 2)
    print("Your score:", science_score)
    print("\n")

    time.sleep(1)

    if science_score == 5:
        print("WOW! ALL QUESTIONS CORRECT!")

    elif science_score == 1:
        print("You got 1 question correct!")

    elif science_score == 0:
        print("You got 0 questions correct")


    else:
        print(f"You got {science_score} questions correct!")


sport()

time.sleep(3)

science_continue = input("Would you like to continue? (y/n): ").lower()
if science_continue == "y" or science_continue == "yes":
    science()
elif science_continue == "n" or science_continue == "no":
    print("Goodbye!")
    time.sleep(1)
    print("closing in", end=" ")
    for closing in reversed(range(1, 4)):
        time.sleep(1)
        print(closing, end=" ")
    time.sleep(1)
    exit()
