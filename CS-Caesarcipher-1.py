def caesar_cipher(cypher_text, shift_value):
    import string # to be able to select the letters and punctuation without declaring them one by one

    # the characters to be shifted: all letters and punctuation
    characters = string.ascii_letters + string.punctuation
    shifted_text = ""

    for char in cypher_text:
        if char in characters:
            char_index = characters.index(char)
            # Perform the shift with wrap-around
            shifted_index = (char_index + shift_value) % len(characters)
            shifted_text += characters[shifted_index]
        else:
            # Leave characters like digits and spaces unchanged
            shifted_text += char

    return shifted_text

def main():
    # create a menu for the users
    while True:
        print("\nCaesar Cipher")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift_amount = int(input("Enter the shift amount: "))
            encrypted = caesar_cipher(message, shift_amount)
            print("Encrypted message:", encrypted)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift_amount = int(input("Enter the shift amount: "))
            decrypted = caesar_cipher(message, -shift_amount)
            print("Decrypted message:", decrypted)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
