student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
min_score = student_scores[0]

for score in student_scores:
    if max_score < score:
        max_score = score
    if min_score > score:
        min_score = score

print(max_score)
print(max(student_scores))
print(min_score)
print(min(student_scores))


