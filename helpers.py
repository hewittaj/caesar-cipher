alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar_cipher(text, shift, direction):
    """
    Decrypts or Encrypts the text given by shifting the letters by the declared number and
    in the direction specified by the user 'e' for encryption 'd' for decryption.
    """
    final_text = []
    new_index = 0
    split_text = list(text)

    for letter in split_text:
        index = alphabet.index(letter)
        # Decrypt text
        if direction == 'd':
            new_index = index - shift
            if new_index < 0:
                new_index = new_index % 26
            final_text.append(alphabet[new_index])
        # Encrypt text
        elif direction == 'e':
            new_index = index + shift
            if new_index > 25:
                new_index = new_index % 26
            final_text.append(alphabet[new_index])

        # Invalid option entered
        else:
            print("Invalid option entered. Please try again.")

    print(''.join(final_text))
