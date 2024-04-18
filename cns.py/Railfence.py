def encrypt_rail_fence(plaintext, rails):
    fence = [[' ' for _ in range(len(plaintext))] for _ in range(rails)]
    direction = 1  # 1 for down, -1 for up
    row, col = 0, 0

    for char in plaintext:
        fence[row][col] = char
        row += direction

        if row == rails - 1 or row == 0:
            direction *= -1

        col += 1

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

def decrypt_rail_fence(ciphertext, rails):
    fence = [[' ' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = 1
    row, col = 0, 0

    for char in ciphertext:
        fence[row][col] = '*'
        row += direction

        if row == rails - 1 or row == 0:
            direction *= -1

        col += 1

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*' and index < len(ciphertext):
                fence[i][j] = ciphertext[index]
                index += 1

    row, col = 0, 0
    direction = 1
    decrypted_text = ''

    for _ in range(len(ciphertext)):
        decrypted_text += fence[row][col]
        row += direction

        if row == rails - 1 or row == 0:
            direction *= -1

        col += 1

    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    rails = int(input("Enter the number of rails: "))

    # Encrypt
    ciphertext = encrypt_rail_fence(plaintext, rails)
    print("Encrypted text:", ciphertext)

    # Decrypt
    decrypted_text = decrypt_rail_fence(ciphertext, rails)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()