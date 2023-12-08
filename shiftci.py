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


def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").strip().upper()
    if choice == 'E':
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value (a positive integer): "))
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value (a positive integer): "))
        decrypted_text = caesar_cipher(text, -shift)  # Decrypt by shifting in the opposite direction
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")


if __name__ == "__main__":
    main()
