def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(message[i])
    return ''.join(key)

def encrypt(message, key):
    encrypted_message = []
    key = generate_key(message, key)
    for i in range(len(message)):
        char = (ord(message[i]) + ord(key[i])) % 26
        encrypted_message.append(chr(char + 65))
        key += chr(char + 65)
    return ''.join(encrypted_message)

def decrypt(encrypted_message, key):
    decrypted_message = []
    key = generate_key(encrypted_message, key)
    for i in range(len(encrypted_message)):
        char = (ord(encrypted_message[i]) - ord(key[i]) + 26) % 26
        decrypted_message.append(chr(char + 65))
        key += encrypted_message[i]
    return ''.join(decrypted_message)

def main():
    message = input("Enter the message to be encrypted: ").replace(" ", "").upper()
    key = input("Enter the encryption key: ").replace(" ", "").upper()
    
    encrypted_message = encrypt(message, key)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()