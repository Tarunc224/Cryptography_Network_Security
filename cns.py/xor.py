# Write a Cprogram that contain sastring (charpointer)with the value ‘Hello world.’ TheprogramshouldXOReachcharacterinthisstringwith0and displays the result. 

def xor_with_zero(input_string):
    
    result = ''.join(chr(ord(char) ^ 0) for char in input_string)
    return result
char_pointer = 'Hello world.'
result_xor_zero = xor_with_zero(char_pointer)
print("Result after XOR with 0:", result_xor_zero)