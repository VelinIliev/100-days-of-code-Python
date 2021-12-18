alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(plain_text, shift_amount, cipher_direction):
    new_message = ""
    if cipher_direction.lower() == "decode":
            shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char) 
            new_position = position + shift_amount
            new_message += alphabet[new_position]
        else: 
            new_message += char
    print(f'The {cipher_direction}d text is {new_message}')

end_of_program = False

while end_of_program == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    cesar(plain_text = text, shift_amount = shift, cipher_direction = direction)
    continue_decoding = input('Type "yes" if you want to go again. Otherwise type "no"\n')
    if continue_decoding.lower() == "no":
        end_of_program = True



# def encrypt(plain_text, shift_amount):
#     encoded_message = ""
#     for letter in plain_text:
#         position = alphabet.index(letter) 
#         new_position = position + shift_amount
#         encoded_message += alphabet[new_position]
#     print(f'The encoded text is: {encoded_message}')

# def decrypt(cipher_text, shift_amount):
#     decoded_message = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decoded_message += alphabet[new_position]
#     print(f"The decoded text is: {decoded_message}")

# if direction.lower() == 'encode':
#      encrypt(plain_text = text, shift_amount = shift)
# elif direction.lower() == "decode":
#     decrypt(cipher_text = text, shift_amount = shift)

