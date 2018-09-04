import random
import time

name = input("What is your name?: ")
print("Hello %s." % name)

g_1 = "The Gods are tilting the scales in your favor, just for you."
g_2 = "The results are very promising."
g_3 = "Things should go well."
n_1 = "The answers are unclear. Come back in a few minutes."
n_2 = "I'm not saying yes...but I'm not saying no."
b_1 = "The answer isn't good."
b_2 = "Give up hope."
b_3 = "I could tell the truth but you're not going to like it."
answers = [g_1,g_2,g_3,n_1,n_2,b_1,b_2,b_3]

while name == name:
    question = input("Ask a yes or no question please(If not type stop to leave): ")
    if question == "stop":
        print("Till we see each other again %s..." % name)
        break
    else:
        print("One moment...")
        time.sleep(3)
        print(random.choice(answers))
