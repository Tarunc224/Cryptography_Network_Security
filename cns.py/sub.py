import random

def generate_substitution_key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

def substitute_text(text, substitution_key):
    return ''.join(substitution_key.get(char, char) for char in text.upper())

if __name__ == "__main__":
    user_text = input("Enter the text to encrypt: ")

    substitution_key = generate_substitution_key()
    encrypted_result = substitute_text(user_text, substitution_key)
    
    print("Substitution Key:", substitution_key)
    print("Encrypted:", encrypted_result)

    decrypted_result = substitute_text(encrypted_result, {v: k for k, v in substitution_key.items()})
    print("Decrypted:", decrypted_result)