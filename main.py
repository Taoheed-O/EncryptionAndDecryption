# from playfairEncryption import encrypt
# from playfairDecryption import decrypt
#
# # Example usage:
# key = "PLAYFAIREXAMPLE"
# plaintext = "HELLO WORLD"
#
# # Encryption
# ciphertext = encrypt(plaintext, key)
# print("Cipher text:", ciphertext)
#
# # Decryption
# decrypted_text = decrypt(ciphertext, key)
# print("Decrypted text:", decrypted_text)
#


from TextToDigraphConverter import convertPlainTextToDiagraphs
from encryption import encryption
from decryption import decryption


def main():
    # Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encrypted)
    key = input("Enter key: ").replace(" ", "").upper()
    plainText = input("Plain Text: ").replace(" ", "").upper()

    convertedPlainText = convertPlainTextToDiagraphs(plainText)
    cipherText = "".join(encryption(convertedPlainText, key))
    cipherText = cipherText.replace(',', '')
    print(cipherText)
    print(decryption(cipherText, key))


if __name__ == "__main__":
    main()
