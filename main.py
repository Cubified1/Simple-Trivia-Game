import random
import time


decor1 = "="
decor1_amount = 20
loading_prog = "."
loading_prog_rand = random.randint(2, 3)

print(decor1 * decor1_amount)
print ("welcome to my simple trivia game")
print(decor1 * decor1_amount)



for load in range(3):
    time.sleep(1)
    loading_prog = loading_prog * loading_prog_rand
    print(f"loading {loading_prog}")


time.sleep(2)

print("\n" * 3)

def sport():
    question_rand = random.randint(0, 4)

    questions = ("How many players are on a basketball team on the court?: ",
                "Which country invented basketball?: ",
                "How many points is a touchdown worth in American football?: ",
                "How many holes are in a standard golf round?: ",
                "Which sport uses a puck?: ")
    for question in questions:
        print(random.choice(questions))


sport()



