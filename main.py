import art
from helpers import caesar_cipher

print(art.logo)
keep_playing = True
direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")

while keep_playing:
    if direction == 'e' or direction == 'd':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar_cipher(text, shift, direction)
        keep_playing = False if input("Would you like to keep playing (y/n)? ") == 'n' else True
        
    else:
        print("Invalid option entered. Please try again.")
