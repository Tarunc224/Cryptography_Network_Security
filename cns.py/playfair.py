import re

def generate_playfair_matrix(key):
    key = re.sub(r'[^a-z]', '', key.lower()) 
    key += 'abcdefghiklmnopqrstuvwxyz' 
    key = ''.join(sorted(set(key), key=key.index))  
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = re.sub(r'[^a-z]', '', plaintext.lower())  
    plaintext = re.sub(r'(.)\1', r'\1x\1', plaintext)  # Double letters become x
    if len(plaintext) % 2 != 0:
        plaintext += 'x'  # Append 'x' if the length is odd
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

def main():
    key = "ldrp"
    plaintext = input("Enter the plaintext: ")

    ciphertext = playfair_encrypt(plaintext, key)
    decrypted_text = playfair_decrypt(ciphertext, key)

    print("\nPlaintext:", plaintext)
    print("Key:", key)
    print("Encrypted Text:", ciphertext)
    print("Decrypted Text:", decrypted_text)

if __name__== "__main__":
    main()