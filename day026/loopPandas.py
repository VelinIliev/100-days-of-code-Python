
student_dict = {
    "students": ["Angela", "James","Lilly"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
    # print(f'{key}: {value}')

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(index, row.students, row.score)