def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char

    return result



text = input("Enter Plaintext: ")
shift = int(input("Enter Shift:"))
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)


decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)
