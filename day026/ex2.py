with open("./file1.txt") as file1:
    file1_contents = file1.readlines()
    file1_data = [int(n.strip()) for n in file1_contents]

with open("./file2.txt") as file2:
    file2_contents = file2.readlines()
    file2_data = [int(n.strip()) for n in file2_contents]

result = [num for num in file1_data if num in file2_data]
print(result)
