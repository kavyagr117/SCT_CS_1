# Function to encrypt the message
def encrypt(text, shift):
    encrypted_message = ""
    
    for char in text:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_message += char  # Non-alphabet characters remain unchanged
            
    return encrypted_message

# Function to decrypt the message
def decrypt(text, shift):
    decrypted_message = ""
    
    for char in text:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted_message += char  # Non-alphabet characters remain unchanged
            
    return decrypted_message

# Main function to interact with the user
def caesar_cipher():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt the message? ").upper()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid option. Please choose 'E' to encrypt or 'D' to decrypt.")

# Run the program
if __name__ == "__main__":
    caesar_cipher()
