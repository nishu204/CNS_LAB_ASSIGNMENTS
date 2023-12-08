def encrypt_rail_fence(text, depth):
    fence = [[' ' for _ in range(len(text))] for _ in range(depth)]
    direction = 1
    row, col = 0, 0

    for char in text:
        fence[row][col] = char
        if row == depth - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
        col += 1

    encrypted_text = ''.join([''.join(row) for row in fence])
    return encrypted_text


def decrypt_rail_fence(encrypted_text, depth):
    fence = [[' ' for _ in range(len(encrypted_text))] for _ in range(depth)]
    direction = 1
    row, col = 0, 0

    for _ in range(len(encrypted_text)):
        fence[row][col] = '*'
        if row == depth - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
        col += 1

    index = 0
    for i in range(depth):
        for j in range(len(encrypted_text)):
            if fence[i][j] == '*' and index < len(encrypted_text):
                fence[i][j] = encrypted_text[index]
                index += 1

    direction = 1
    row, col = 0, 0
    decrypted_text = ''

    for _ in range(len(encrypted_text)):
        decrypted_text += fence[row][col]
        if row == depth - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
        col += 1

    return decrypted_text


def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").strip().upper()
    if choice == 'E':
        text = input("Enter the text to encrypt: ")
        depth = int(input("Enter the depth of the Rail Fence: "))
        encrypted_text = encrypt_rail_fence(text, depth)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        encrypted_text = input("Enter the text to decrypt: ")
        depth = int(input("Enter the depth of the Rail Fence: "))
        decrypted_text = decrypt_rail_fence(encrypted_text, depth)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")


if __name__ == "__main__":
    main()
