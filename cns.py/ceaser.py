#W eek-3: i.Write a Java program to perform encryption and decryption using the following algorithms a. Ceaser cipher
def encrypt_ceasar(plaintext, shift):
    result = ""

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

def decrypt_ceasar(ciphertext, shift):
    return encrypt_ceasar(ciphertext, -shift)

plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

ciphertext = encrypt_ceasar(plaintext, shift)
print("Encrypted:", ciphertext)

decrypted_text = decrypt_ceasar(ciphertext, shift)
print("Decrypted:", decrypted_text)