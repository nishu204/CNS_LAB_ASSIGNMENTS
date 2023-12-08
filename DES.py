from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext


def decrypt_des(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext)


def pad(text):
    block_size = DES.block_size
    padding_size = block_size - (len(text) % block_size)
    padding = bytes([padding_size] * padding_size)
    return text + padding


def unpad(text):
    padding_size = text[-1]
    return text[:-padding_size]


def main():
    password = input("Enter a password: ").encode('utf-8')
    salt = get_random_bytes(8)
    key = PBKDF2(password, salt, dkLen=8, count=1000000)

    plaintext = input("Enter the plaintext: ").encode('utf-8')

    ciphertext = encrypt_des(key, plaintext)
    print("Encrypted:", ciphertext.hex())

    decrypted_text = decrypt_des(key, ciphertext)
    print("Decrypted:", decrypted_text.decode('utf-8'))


if __name__ == "__main__":
    main()
