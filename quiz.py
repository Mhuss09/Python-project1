print("Welcome to the Python Quiz!")

def thanks():
    print("Thanks for trying out my python quiz!")

def score_result(score):
    if score == 0:
        print("Try again your score was", score)
    if score == 1:
        print("Try better next time your score was", score)
    elif score == 2:
        print("Good Try, do better next time, your score was", score)
    elif score >=3:
        print("Well done, your score was", score)
    thanks()

def quiz():
    score = 0
    answer = input("What is the capital of france? is it A: Berlin, B: Madrid, C: Paris, D: Rome ? ")
    if answer == "C":
        print("Correct! you have earned a point.")
        score = score + 1
    else:
        print("Wrong! You have not earned a point")
        
    answer = input("What is the capital of Morocco? is it A: Rabat, B: Madrid, C: Paris, D: Rome ? ")
    if answer == "A":
        print("Correct! you have earned a point.")
        score = score + 1
    else:
        print("Wrong! You have not earned a point")

    answer = input("What is the capital of Belgium? is it A: Berlin, B: Brussels, C: Paris, D: Rome ? ")
    if answer == "B":
        print("Correct! you have earned a point.")
        score = score + 1
    else:
        print("Wrong! You have not earned a point")

    answer = input("What is the capital of Germany? is it A: Berlin, B: Madrid, C: Paris, D: Rome ? ")
    if answer == "A":
        print("Correct! you have earned a point.")
        score = score + 1
    else:
        print("Wrong! You have not earned a point")
    score_result(score)

quiz()



