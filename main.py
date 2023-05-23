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
    # converting the plaintext into digraphs
    convertedPlainText = convertPlainTextToDiagraphs(plainText)
    # encryption of the text and conversion into a cipher text
    cipherText = "".join(encryption(convertedPlainText, key))
    cipherText = cipherText.replace(',', '')
    print('playFair cipher Encoded text: ', cipherText)

    # passing this text into the second cipher encryption known as the rail fence cipher
    # using 3 rails by default
    railfenceCipherText = encryptRailFence(cipherText, 3)
    print("Rail Fence encrypted text : ", railfenceCipherText)

    # decrypting the railfence cipher first by passing it through the railFence decryption cipher
    railfenceDecryptedText = decryptRailFence(railfenceCipherText, 3)
    print("Rail Fence decrypted text : ", railfenceDecryptedText)

    # passing this through the playfair decryption cipher function
    decryptedText = decryption(railfenceDecryptedText, key)
    # print('playfair Cipher Decoded text: ', decryptedText)

    decryptedText = [x for x in decryptedText if x != ',']
    digraphText = group(decryptedText, 2)

    # returning the whole text in uppercase...
    newText = convertDigraphsToPlainText(list(digraphText))
    print('original text: ', separator(newText))


if __name__ == "__main__":
    main()
