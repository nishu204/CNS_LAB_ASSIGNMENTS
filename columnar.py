def encrypt_columnar_transposition(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = -(-len(text) // num_columns)
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    for i, char in enumerate(text):
        row = i // num_columns
        col = key_order[i % num_columns]
        matrix[row][col] = char

    encrypted_text = ''.join([''.join(row) for row in matrix])
    return encrypted_text

def decrypt_columnar_transposition(encrypted_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = -(-len(encrypted_text) // num_columns)
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    index = 0
    for col in key_order:
        for row in range(num_rows):
            if index < len(encrypted_text):
                matrix[row][col] = encrypted_text[index]
                index += 1

    decrypted_text = ''.join([''.join(row) for row in matrix])
    return decrypted_text

# def decrypt_columnar_transposition(encrypted_text, key):
#     key_order = sorted(range(len(key)), key=lambda k: key[k])
#     num_columns = len(key)
#     num_rows = -(-len(encrypted_text) // num_columns)
#     matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
#
#     index = 0
#     for col in key_order:
#         for row in range(num_rows):
#             matrix[row][col] = encrypted_text[index]
#             index += 1
#
#     decrypted_text = ''.join([''.join(row) for row in matrix])
#     return decrypted_text


def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").strip().upper()
    if choice == 'E':
        text = input("Enter the text to encrypt: ")
        key = input("Enter the key (e.g., 3124): ")
        encrypted_text = encrypt_columnar_transposition(text, key)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        encrypted_text = input("Enter the text to decrypt: ")
        key = input("Enter the key (e.g., 3124): ")
        decrypted_text = decrypt_columnar_transposition(encrypted_text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")


if __name__ == "__main__":
    main()
