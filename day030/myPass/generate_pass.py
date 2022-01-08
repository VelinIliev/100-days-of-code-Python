from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_random_password(nr_letters=8, nr_numbers=2, nr_symbols=2):
    """Genrate random password with arguments.
    You can define leters: nr_leters, numbers: nr_numbers and symbols: nr_symbols """
    new_password = [choice(letters) for _ in range(1, nr_letters) ]
    new_password += [choice(numbers) for _ in range(1, nr_numbers) ]
    new_password += [choice(symbols) for _ in range(1, nr_symbols) ]

    shuffle(new_password)
    password = ''.join(new_password)    

    return password