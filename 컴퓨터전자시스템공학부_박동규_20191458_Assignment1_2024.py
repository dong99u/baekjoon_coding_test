def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Example usage:
plaintext = input()
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print("Encrypted:", ciphertext)

# To decrypt, use the negative of the original shift
decrypted_text = caesar_cipher(ciphertext, -shift)
print("Decrypted:", decrypted_text)
