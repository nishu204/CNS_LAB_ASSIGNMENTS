def vigenere_cipher(text, key):
    text = text.upper()
    key = key.upper()
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            encrypted_char = chr(((ord(text[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += text[i]

    return encrypted_text


def vigenere_decipher(text, key):
    text = text.upper()
    key = key.upper()
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr(((ord(text[i]) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += text[i]

    return decrypted_text


def main():
    key = "KEY"
    plaintext = "HELLO WORLD"

    encrypted_text = vigenere_cipher(plaintext, key)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = vigenere_decipher(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
