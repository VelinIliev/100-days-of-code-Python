def my_function():
    result = 3 * 2 
    return result

def format_name(f_name, l_name):
    """"Take a first and last name and format it
     to return the title case version of the name. """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"

    first_name = f_name.title()
    last_name = l_name.capitalize()
    # name = first_name + " " + last_name
    return f'{first_name} {last_name}'

print(format_name(f_name = "velin", l_name = "ILIEV"))