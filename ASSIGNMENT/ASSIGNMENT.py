
course1 = float(input("input your score for Mathematics: "))
course2 = float(input("input your score for English Language: "))
course3 = float(input("input your score for Physic: "))
course4 = float(input("input your score for Chemistry: "))
course5 = float(input("input your score for Biology: "))
course6 = float(input("input your score for Financial Accounting "))
course7 = float(input("input your score for Agric science"))
course8 = float(input("input your score for Computer science"))
course9 = float(input("input your score for Economics"))

Aggregate=(course1+course2+course3+course4+course4+course6+course7+course8+course9)/9

total = course1 + course2 + course3 + course4 + course5 + course6 + course7 + course8 + course9
Aggregate = total / 9
print(Aggregate)

# Criteria for admission score
if Aggregate >= 80:
    print('Admission into Faculty of Medicine and Law')
elif 75 <= Aggregate <= 79:
    print("Admission into Faculty of Banking and Finance, Insurance and Accountancy")
elif 71 <= Aggregate <= 74:
    print("Admission into Faculty of Pharmacy, Physiology, Pharmacology and Nursing")
elif 61 <= Aggregate <= 70:
    print("Admission into Faculty of Computer Science, Psychology and Statistics")
elif 55 <= Aggregate <= 60:
    print("Admission into Faculty of Botany, Zoology")
elif 50 <= Aggregate <= 54:
    print("Admission into Faculty of Agricultural Science department")
else:
    print("No admission")


import pygame
