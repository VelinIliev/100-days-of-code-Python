student_heights = [180, 124, 165, 173, 189, 169, 146]
sum = 0
count = 0

# do not use sum() or len()

for height in student_heights:
    count += 1
    sum += height

average = round((sum / count))
print(average)