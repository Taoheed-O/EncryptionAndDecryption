from TextToDigraphConverter import convertPlainTextToDiagraphs
from playFairEncryption import encryption
from playFairDecryption import decryption
from decryptedTextToDigraph import group
from DigraphToTextConverter import convertDigraphsToPlainText
from separator import separator
from railFenceEncryption import encryptRailFence
from railFenceDecryption import decryptRailFence


def main():
    # Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encrypted)
    key = input("Enter key: ").replace(" ", "").upper()
    plainText = input("Plain Text: ").replace(" ", "").upper()

    convertedPlainText = convertPlainTextToDiagraphs(plainText)
    cipherText = "".join(encryption(convertedPlainText, key))
    cipherText = cipherText.replace(',', '')
    print('Encoded text: ', cipherText)

    decryptedText = decryption(cipherText, key)
    print('Decoded text: ', decryptedText)

    decryptedText = [x for x in decryptedText if x != ',']
    digraphText = group(decryptedText, 2)

    newText = convertDigraphsToPlainText(list(digraphText))
    print('original text: ', separator(newText))




    print(encryptRailFence("attack at once", 2))
    print(encryptRailFence("GeeksforGeeks ", 3))
    print(encryptRailFence("defend the east wall", 3))

    # Now decryption of the
    # same cipher-text
    print(decryptRailFence("GsGsekfrek eoe", 3))
    print(decryptRailFence("atc toctaka ne", 2))
    print(decryptRailFence(encryptRailFence("defend the east wall", 3), 3))


if __name__ == "__main__":
    main()
