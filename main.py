from helpers import caesar_cipher

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")

if direction == 'e' or direction == 'd':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)

else:
    print("Invalid option entered. Please try again.")
