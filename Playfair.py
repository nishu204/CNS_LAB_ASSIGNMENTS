def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_set = set(key)
    matrix = ""

    for char in key:
        if char not in matrix:
            matrix += char

    for char in alphabet:
        if char not in matrix and char not in key_set:
            matrix += char

    matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    return matrix

def find_coordinates(matrix, char):
    for row in range(5):
        if char in matrix[row]:
            col = matrix[row].index(char)
            return row, col

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.replace(" ", "").upper()
    encrypted_text = ""

    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = ""
        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]

        if char1 == char2:
            char2 = "X"
            i += 1

        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return encrypted_text

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""

    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)

        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return decrypted_text

def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").strip().upper()
    if choice == 'E':
        plaintext = input("Enter the plaintext to encrypt: ")
        key = input("Enter the key: ")
        encrypted_text = playfair_encrypt(plaintext, key)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        ciphertext = input("Enter the ciphertext to decrypt: ")
        key = input("Enter the key: ")
        decrypted_text = playfair_decrypt(ciphertext, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
