import math

def columnar_transposition(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)

    # Fill the grid with placeholders
    grid = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill the grid with text
    for i, char in enumerate(text):
        row = i // num_cols
        col = key_order[i % num_cols]
        grid[row][col] = char

    # Read the grid column-wise
    encrypted_text = ''
    for col in range(num_cols):
        for row in range(num_rows):
            encrypted_text += grid[row][col]

    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ").replace(" ", "").upper()
    key = input("Enter the key for columnar transposition: ").replace(" ", "").upper()

    encrypted_text = columnar_transposition(text, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()