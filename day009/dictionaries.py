programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
    123: "Test"
    }

print(programming_dictionary['Loop'])
print(programming_dictionary[123])

programming_dictionary["new_key"] = "Test2"
print(programming_dictionary)

empty_dictonary = {}
programming_dictionary["Bug"] = "A moth in your computer"

for key in programming_dictionary:
    print(f'{key}: {programming_dictionary[key]}')