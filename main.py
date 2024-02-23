# start off with generating 5 problems, eventually expand to max 10

import math1
import random

exam = []
answers = []
score = 0
for n in range(5):
    math1.generate_exam(exam, answers)
print("Your generated exam is:")
print(answers)
for n in range(len(exam)):
    print(f"{n+1}) {exam[n]}")

math1.grade(exam, answers, score)




