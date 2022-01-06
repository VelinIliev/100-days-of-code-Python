
import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
# new_data = data.to_dict('records')
phonetic_alphabet = {row.letter: row.code for (index,row) in data.iterrows()}
# for x in data.to_dict('records'):
#     phonetic_alphabet[x["letter"]] = x["code"]
    
# print(phonetic_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# name_to_spell = input("Enter name:")
# name_arr = [letter for letter in input("Enter name:").upper()]

# final_array = []
# for letter in name_arr:
#     for (key,value) in phonetic_alphabet.items():
#         if letter == key:
#             final_array.append(value)

output_list = [phonetic_alphabet[letter] for letter in input("Enter name:").upper()]

print(output_list)
