alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(text, shift):
    """
    Decrypts the text given by shifting the letters back by the declared number.
    """
    pass

def encrypt(text, shift):
    """
    Encrypts the text given by shifting the letters by the declared number.
    """
    encrypted_text = []
    new_index = 0
    split_text = list(text)
    for letter in split_text:
        index = alphabet.index(letter)
        new_index = index + shift
        if new_index > 25:
            new_index = new_index % 26
        encrypted_text.append(alphabet[new_index])
    print(''.join(encrypted_text))