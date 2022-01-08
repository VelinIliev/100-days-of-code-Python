
import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (index,row) in data.iterrows()}

while True:
    try:
        output_list = [phonetic_alphabet[letter] for letter in input("Enter name:").upper()]
    except KeyError:
        print("please enter only letters")
    else:
        print(output_list)
        break

def generate_phonetic():
    try:
        output_list = [phonetic_alphabet[letter] for letter in input("Enter name:").upper()]
    except KeyError:
        print("please enter only letters")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()

