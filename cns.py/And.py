def and_or_xor_with_127(input_string, operation):
    if operation not in ['and', 'or', 'xor']:
        raise ValueError("Invalid operation. Use 'and', 'or', or 'xor'.")

    if operation == 'and':
        result = ''.join(chr(ord(char) & 127) for char in input_string)
    elif operation == 'or':
        result = ''.join(chr(ord(char) | 127) for char in input_string)
    elif operation == 'xor':
        result = ''.join(chr(ord(char) ^ 127) for char in input_string)

    return result

# Declare a string with the value 'Hello world.'
char_pointer = 'Hello world.'

# Apply AND, OR, or XOR with 127 to each character
operation = 'and'  # Change this to 'and' or 'or' as needed
result_and_or_xor_127 = and_or_xor_with_127(char_pointer, operation)

# Display the result
print(f"Result after {operation.upper()} with 127:", result_and_or_xor_127)