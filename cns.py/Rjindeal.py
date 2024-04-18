from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def rijndael_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def rijndael_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    unpadded_decrypted = unpad(decrypted, AES.block_size)
    return unpadded_decrypted

def main():
    key = get_random_bytes(16)
    
    plaintext = input("Enter the plaintext: ").encode('utf-8')

    encrypted = rijndael_encrypt(key, plaintext)
    decrypted = rijndael_decrypt(key, encrypted)

    print("Plaintext:", plaintext.decode('utf-8'))
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode('utf-8'))

if __name__ == "__main__":
    main()