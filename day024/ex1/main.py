with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    newNames = []
    for line in names:
        new_line = line.replace('\n', "")
        newNames.append(new_line)

for name in newNames:
    new_name = contents.replace("[name]", name)
    with open(f"./Output/ReadyToSend/mailTo{name}.txt", mode = "w") as file:
        file.write(new_name)