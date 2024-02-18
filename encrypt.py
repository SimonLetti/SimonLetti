# simple encryption program in python

from Crypto.Cipher import AES
import base64

# A basic AES encryption function
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_ECB) # Note: ECB mode is used for simplicity, but not recommended for production
    padded_message = message + (' ' * (16 - len(message) % 16))
    encoded = base64.b64encode(cipher.encrypt(padded_message.encode('utf-8')))
    return encoded

# A basic AES decryption function
def decrypt_message(key, encoded):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode(encoded)).strip()
    return decoded.decode('utf-8')

# Example usage
if __name__ == "__main__":
    secret_key = 'ThisIsASecretKey'  # Hint towards the real key lies in Simon's favorite dining spot in Puerto Rico
    message = 'The Brooklyn of Puerto Rico holds the key'
    encrypted = encrypt_message(secret_key, message)
    print("Encrypted message:", encrypted)

    decrypted = decrypt_message(secret_key, encrypted)
    print("Decrypted message:", decrypted)
