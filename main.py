import random
import time


decor1 = "="
decor1_amount = 20
loading_prog = "."
loading_prog_rand = random.randint(1, 3)

print(decor1 * decor1_amount)
print ("welcome to my simple trivia game")
print(decor1 * decor1_amount)



for load in range(3):
    time.sleep(1)
    loading_prog = loading_prog * loading_prog_rand
    print(f"loading {loading_prog}")
