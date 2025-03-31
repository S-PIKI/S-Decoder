# Program: Practical 4 - Decoder

# List of ASCII values
ascii_Values = [67, 73, 83, 45, 49, 57, 48, 123, 77, 97, 115, 116, 101, 114, 105, 110, 103, 95, 67, 104, 114, 125]

# Convert ASCII values to characters
secret_Message = ""
for number in ascii_Values:
    secret_Message += chr(number)

# Print the secret message
print("Secret Message:", secret_Message)