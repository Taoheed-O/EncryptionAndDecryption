# Function to decrypt an already rail-fenced encrypted text

# This function receives cipher-text and key and returns the original text after decryption
def decryptRailFence(cipher, key):
    # create the matrix to cipher plain text key = rows , length(text) = columns filling the rail matrix to
    # distinguish filled spaces from blank ones
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    # finding the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # placing the marker
        rail[row][col] = '*'
        col += 1

        # finding the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the *fill the rail matrix*
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # reading the matrix in zig-zag format to construct the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        # checking the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # placing the marker
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)
