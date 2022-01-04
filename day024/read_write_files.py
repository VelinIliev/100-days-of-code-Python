# file = open("test.txt") as file:
# contents = file.read()
# print(contents)
# file.close()

with open("./test.txt") as file:
    contents = file.read()
    print(contents)

# mode "r" - read only

# mode "w" - write, will delete all previous content
    # if file do not exist, will crate new with the name

# mode "a" - append to the previous content

with open("./test.txt", mode = "a") as file:
    file.write("\nNew text.")

with open("./test.txt") as file:
    contents = file.read()
    print(contents)