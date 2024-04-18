#Encrypt the message “PAY” using hill cipherwith the following keymatrix and show the decryption to formulate original plaintext
import numpy as np

# Define the key matrix
key_matrix = np.array([[17, 17, 5],
                       [21, 18, 21],
                       [2, 2, 19]])

# Function to encrypt a message using Hill cipher
def hill_encrypt(plaintext, key_matrix):
    # Convert plaintext to numbers
    plaintext = plaintext.upper()
    plaintext = [ord(char) - 65 for char in plaintext]

    # Padding if necessary
    if len(plaintext) % len(key_matrix) != 0:
        padding_length = len(key_matrix) - (len(plaintext) % len(key_matrix))
        plaintext += [23] * padding_length  # 23 represents 'X' in ASCII

    # Reshape plaintext into matrix
    plaintext_matrix = np.array(plaintext).reshape(-1, len(key_matrix))

    # Encrypt each block
    encrypted_blocks = []
    for block in plaintext_matrix:
        encrypted_block = np.dot(block, key_matrix) % 26
        encrypted_blocks.append(encrypted_block)

    # Convert encrypted blocks back to characters
    encrypted_text = ''.join([chr(block + 65) for block in np.concatenate(encrypted_blocks)])

    return encrypted_text

# Function to decrypt a message using Hill cipher
def hill_decrypt(ciphertext, key_matrix):
    # Convert ciphertext to numbers
    ciphertext = ciphertext.upper()
    ciphertext = [ord(char) - 65 for char in ciphertext]

    # Reshape ciphertext into matrix
    ciphertext_matrix = np.array(ciphertext).reshape(-1, len(key_matrix))

    # Calculate the modular inverse of the key matrix
    det = int(np.round(np.linalg.det(key_matrix)))
    inv_det = pow(det, -1, 26)  # Modular inverse of det modulo 26
    key_matrix_inv = (inv_det * np.round(det * np.linalg.inv(key_matrix)).astype(int)) % 26

    # Decrypt each block
    decrypted_blocks = []
    for block in ciphertext_matrix:
        decrypted_block = np.dot(block, key_matrix_inv) % 26
        decrypted_blocks.append(decrypted_block)

    # Convert decrypted blocks back to characters
    decrypted_text = ''.join([chr(block + 65) for block in np.concatenate(decrypted_blocks)])

    return decrypted_text

# Get the plaintext from the user
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext
encrypted_text = hill_encrypt(plaintext, key_matrix)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text to obtain the original plaintext
decrypted_text = hill_decrypt(encrypted_text, key_matrix)
print("Decrypted:", decrypted_text)