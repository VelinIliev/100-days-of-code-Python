import random
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {name: random.randint(1,100) for name in names}

print(students_scores)

passed_students = {name: score for (name,score) in students_scores.items() if score >= 60}

print(passed_students)