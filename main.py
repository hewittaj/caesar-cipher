from helpers import decrypt, encrypt

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
    
if direction == 'e':
    encrypt(text, shift)
elif direction == 'd':
    decrypt(text, shift)
else:
    print("Invalid option entered. Please try again.")