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
from playFairEncryption import encryption
from playFairDecryption import decryption
from decryptedTextToDigraph import group
from DigraphToTextConverter import convertDigraphsToPlainText
# from separator import separator


def main():
    # Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encrypted)
    key = input("Enter key: ").replace(" ", "").upper()
    plainText = input("Plain Text: ").replace(" ", "").upper()

    convertedPlainText = convertPlainTextToDiagraphs(plainText)
    cipherText = "".join(encryption(convertedPlainText, key))
    cipherText = cipherText.replace(',', '')
    print(cipherText)

    decryptedText = decryption(cipherText, key)
    print(decryptedText)

    decryptedText = [x for x in decryptedText if x != ',']
    digraphText = group(decryptedText, 2)

    newText = convertDigraphsToPlainText(list(digraphText))
    print(newText)


if __name__ == "__main__":
    main()
