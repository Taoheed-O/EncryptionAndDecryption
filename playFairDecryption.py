from indexLocator import indexLocator
from keyMatrixGenerator import generateKeyMatrix


def decryption(cipherText, key):
    # Decrypt the given cipher text using the Playfair cipher
    keyMatrix = generateKeyMatrix(key)
    plainText = []
    i = 0
    while i < len(cipherText):
        n1 = indexLocator(cipherText[i], keyMatrix)
        n2 = indexLocator(cipherText[i+1], keyMatrix)

        # 2.2  if same column then look in below row so
        # format is [row,col]
        # now to see below row => increase the row in both item
        # (n1[0]+1,n1[1]) => (3+1,1) => (4,1)

        # (n2[0]+1,n2[1]) => (4+1,1) => (5,1)

        # but in our matrix we have 0 to 4 indexes only
        # so to make value bound under 0 to 4 we will do %5
        # i.e.,
        #   (n1[0]+1 % 5,n1[1])
        #   (n2[0]+1 % 5,n2[1])

        if n1[1] == n2[1]:
            i1 = (n1[0] - 1) % 5
            j1 = n1[1]

            i2 = (n2[0] - 1) % 5
            j2 = n2[1]
            plainText.append(keyMatrix[i1][j1])
            plainText.append(keyMatrix[i2][j2])
            plainText.append(",")

        # same row
        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] - 1) % 5

            i2 = n2[0]
            j2 = (n2[1] - 1) % 5
            plainText.append(keyMatrix[i1][j1])
            plainText.append(keyMatrix[i2][j2])
            plainText.append(",")

        # if making rectangle then
        # [4,3] [1,2] => [4,2] [3,1]
        # exchange columns of both value
        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            plainText.append(keyMatrix[i1][j2])
            plainText.append(keyMatrix[i2][j1])
            plainText.append(",")

        i += 2
    return plainText

