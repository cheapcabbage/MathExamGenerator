import random


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


# list for operations
operations = {"+": add,
              "-": subtract,
              "/": divide,
              "*": multiply,
              }


# randint(x, y) generates a random int in the range (x, y) both included
def generate_num():
    return random.randint(1, 9)


# append generated random int and random operation to list exam
def generate_exam(exam, answers):
    s = ""
    x = generate_num()
    y = generate_num()
    # chooses a random key from my operations dic
    z = random.choice(list(operations.keys()))
    # creates the problem as a string and appends  to the exam list
    s = str(x) + " " + z + " " + str(y)
    exam.append(s)
    result = round(operations[z](x, y), 2)
    answers.append(result)


def letter_grade(num):
    if num == 1:
        return "A+"
    elif 1 > num >= 0.9:
        return "A"
    elif 0.9 > num >= 0.8:
        return "B"
    elif 0.9 > num >= 0.7:
        return "C"
    elif 0.7 > num >= 0.6:
        return "D"
    else:
        return "F"


def grade(exam, answers, score):
    for n in range(len(exam)):
        print(f"Starting with problem {n}: {exam[n]}")
        answer = int(input("What is your answer?"))
        if answer == answers[n]:
            score += 1
            print(f"Correct! Your score is {score}/5")
        else:
            print(f"Incorrect. Your score is {score}/5")
    print(f"You missed {5 - score} problems and got {score} correct! Your final grade is {score / 5} "
          f"or {letter_grade(score)}!")
