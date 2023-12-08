from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

# Encryption
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce

print("Original Data:", data)
print("Key:", key)
print("Encrypted Data:", ciphertext)
print("Tag:", tag)
print("Nonce:", nonce)

# Decryption
cipher = AES.new(key, AES.MODE_EAX, nonce)
decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

print("\nDecrypted Data:", decrypted_data.decode('utf-8'))
