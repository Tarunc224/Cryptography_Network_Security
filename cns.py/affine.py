def encrypt_affine_cipher(plaintext):
    """
    Encrypts the given plaintext using the Affine Cipher.
    :param plaintext: The input string to be encrypted.
    :return: The ciphertext.
    """
    a = 3  # Coefficient for the linear transformation
    b = 12  # Constant shift
    m = 26  # Size of the alphabet (assuming a 26-character alphabet)

    # Encryption function: E(x) = (ax + b) mod m
    def encrypt_char(char):
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            encrypted_value = (a * x + b) % m
            return chr(encrypted_value + ord('A'))
        else:
            return char

    ciphertext = "".join(encrypt_char(c) for c in plaintext)
    return ciphertext

def main():
    plaintext = input("Enter the plaintext: ")
    ciphertext = encrypt_affine_cipher(plaintext)
    print(f"Ciphertext: {ciphertext}")

if __name__== "__main__":
    main()