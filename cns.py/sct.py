def encrypt(message, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = (len(message) + num_columns - 1) // num_columns
    pad_length = num_rows * num_columns - len(message)
    padded_message = message + ' ' * pad_length
    encrypted_message = ''
    for i in key_order:
        encrypted_message += padded_message[i::num_columns]
    return encrypted_message

def decrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    plaintext = [''] * num_rows
    for i, k in enumerate(key_order):
        start = i * num_rows
        end = (i + 1) * num_rows
        plaintext[start:end] = ciphertext[i::num_columns]
    return ''.join(plaintext).rstrip()

# Example usage
plaintext = input("Enter the string: ")
key = input("Enter the key: ")  # Example key
encrypted_text = encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)